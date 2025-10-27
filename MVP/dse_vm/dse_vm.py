# dse_vm.py -- minimal DSE-ASM VM + assembler
import json
import time
from collections import defaultdict

class DSEVM:
    def __init__(self):
        self.reg = [0]*8  # R0..R7
        self.PC = 0
        self.SP = 1024
        self.FLAG = 0
        self.COERENCE = 0
        self.ENERGY = 10000
        self.memory = defaultdict(int)
        self.labels = {}
        self.code = []
        self.ledger = {}  # receipts
        self.next_receipt_id = 1
        self.contracts = {}
        self.next_contract_id = 1

    # assembler stores instructions as tuples: (op, *args)
    def load_code(self, code):
        # two pass: resolve labels
        lines = [ln.strip() for ln in code.splitlines() if ln.strip() and not ln.strip().startswith(';')]
        # first pass labels
        pc = 0
        for ln in lines:
            if ln.endswith(':'):
                self.labels[ln[:-1]] = pc
            else:
                pc += 1
        # second pass instructions
        for ln in lines:
            if ln.endswith(':'): continue
            parts = [p.strip() for p in ln.split(None, 1)]
            op = parts[0].upper()
            args = []
            if len(parts) > 1:
                # naive split by comma
                args = [a.strip().strip('"') for a in parts[1].split(',')]
            self.code.append((op, *args))

    def get_reg_index(self, token):
        token = token.upper()
        if token.startswith('R') and token[1:].isdigit():
            i = int(token[1:])
            if 0 <= i < len(self.reg): return i
        raise ValueError("Bad register: "+token)

    def read_value(self, token):
        token = token.strip()
        if token.upper().startswith('R') and token[1:].isdigit():
            return self.reg[self.get_reg_index(token)]
        # try number
        try:
            if '.' in token:
                return float(token)
            return int(token)
        except:
            # label or string or const
            if token in self.labels: return self.labels[token]
            try:
                return int(token)  # fallback
            except:
                return token

    def write_reg(self, regtok, value):
        self.reg[self.get_reg_index(regtok)] = value

    def run(self, max_steps=10000):
        steps = 0
        while self.PC < len(self.code) and steps < max_steps:
            instr = self.code[self.PC]
            op = instr[0]
            args = instr[1:]
            # Debug:
            # print(self.PC, instr)
            self.PC += 1
            steps += 1
            if op == 'MOV':
                dst, src = args
                val = self.read_value(src)
                self.write_reg(dst, val)
            elif op == 'ADD':
                dst, src = args
                val = self.read_value(dst) + self.read_value(src)
                self.write_reg(dst, val)
            elif op == 'SUB':
                dst, src = args
                val = self.read_value(dst) - self.read_value(src)
                self.write_reg(dst, val)
            elif op == 'CMP':
                r, s = args
                a = self.read_value(r); b = self.read_value(s)
                self.FLAG = 1 if a==b else (2 if a>b else 0)
            elif op == 'JMP':
                tgt = args[0]
                self.PC = int(self.read_value(tgt))
            elif op == 'JZ':
                tgt = args[0]
                if self.FLAG == 1:
                    self.PC = int(self.read_value(tgt))
            elif op == 'JNZ':
                tgt = args[0]
                if self.FLAG != 1:
                    self.PC = int(self.read_value(tgt))
            elif op == 'PRINT':
                val = args[0]
                # print register value or literal
                if val.upper().startswith('R'):
                    print(self.read_value(val))
                else:
                    print(val)
            elif op == 'HALT':
                print("HALT")
                break
            # --- DSE primitives ---
            elif op == 'CONTRACT':
                out = args[0]
                cid = self.next_contract_id; self.next_contract_id += 1
                # create a trivial contract record
                self.contracts[cid] = {'created':time.time(), 'meta': None}
                self.write_reg(out, cid)
            elif op == 'OBSERVE':
                out = args[0]
                # produce a simple synthetic observation id
                obs = int(time.time()) % 100000
                self.write_reg(out, obs)
            elif op == 'DERIVE':
                dst, src = args
                obs = self.read_value(src)
                # trivial policy id = obs + 1
                pid = obs + 1
                self.write_reg(dst, pid)
            elif op == 'APPLY':
                policy = args[0]
                val = self.read_value(policy)
                # applying influences coherence a bit
                self.COERENCE = min(10000, self.COERENCE + (val % 10))
            elif op == 'RECEIPT':
                dst, meta = args
                rid = self.next_receipt_id; self.next_receipt_id += 1
                rec = {'id':rid, 'ts':time.time(), 'meta':meta}
                self.ledger[rid] = rec
                self.write_reg(dst, rid)
            elif op == 'VALIDATE':
                # set FLAG=1 if coherence >= target (R0 expected contains target)
                target = self.reg[0]
                self.FLAG = 1 if self.COERENCE >= target else 0
            elif op == 'RESOLVE':
                c_reg, p_reg = args
                # trivial resolve: nudge coherence
                self.COERENCE += 5
            elif op == 'SYNC':
                agent = args[0]
                # noop in this tiny vm
            else:
                raise RuntimeError("Unknown op: "+op)
        else:
            if steps >= max_steps: print("Max steps reached")

if __name__ == '__main__':
    program = '''
    ; example
    MOV R0, 9540
    CONTRACT R1
    main_loop:
    OBSERVE R2
    DERIVE R3, R2
    APPLY R3
    RECEIPT R4, "auto"
    VALIDATE
    JZ ok
    RESOLVE R1, R3
    JMP main_loop
    ok:
    PRINT "Coherence OK, stopping"
    HALT
    '''
    vm = DSEVM()
    vm.load_code(program)
    vm.run()
    print("Final coherence:", vm.COERENCE)
    print("Ledger:", json.dumps(vm.ledger, indent=2))
