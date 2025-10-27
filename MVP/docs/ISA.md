# DSE-ASM Instruction Set Architecture (ISA) Specification

**Version**: 1.0  
**Date**: 2025  
**Author**: OBINexus Computing  
**Repository**: github.com/obinexus/dse-asm

---

## 1. Design Philosophy

DSE-ASM is an assembly language designed for **human-centric constitutional computing** within the OBINexus framework. Unlike traditional assembly languages focused purely on machine efficiency, DSE-ASM prioritizes:

1. **Constitutional Compliance**: Every instruction can be audited for policy adherence
2. **Coherence Maintenance**: Built-in SemVerX system maintains 95.4% minimum coherence
3. **Witness Traceability**: All operations generate observer-witness records
4. **Gating Model**: Instructions based on human cognition (gate-open/gate-close)
5. **No-Ghosting**: Deterministic execution with complete state visibility

### 1.1 Core Principles from OBINexus

```
┌─────────────────────────────────────────────────────┐
│  Invariant Policies (Non-Negotiable Human Rights)  │
├─────────────────────────────────────────────────────┤
│  - Housing: Ages 18-25 free under Act 2014         │
│  - Food: 2-5 meals/day minimum                     │
│  - Water: Continuous access                        │
│  - Shelter: 2.5 miles live-to-work maximum         │
│  - NO entrapment: DELAY/DENY/DEFEND/DEFER illegal  │
└─────────────────────────────────────────────────────┘
```

These invariant policies are **enforced at the instruction level** via `INV.CHECK` operations.

---

## 2. Register Architecture

### 2.1 General Purpose Registers (64-bit)

```
r0  - r15   : General purpose registers
              r0 is NOT special (unlike some ISAs)
              All 16 registers are symmetric
```

### 2.2 Special Purpose Registers

```
pc          : Program Counter (instruction pointer)
sp          : Stack Pointer
fp          : Frame Pointer
lr          : Link Register (for function calls)
flags       : Status Flags Register
```

### 2.3 Constitutional Computing Registers

These registers are **unique to DSE-ASM** and support the OBINexus constitutional framework:

```
obs         : Observer State Register
              Tracks current observation context
              
wit         : Witness Accumulator
              Accumulates witness records for ledger
              
coh         : Coherence Score Register (float 0.0-1.0)
              Real-time coherence measurement
              Updated after each instruction
              
ring        : Ring Zone Identifier (0-7)
              Current constitutional zone:
              0 = Council (central authority)
              1 = Life/Work zone (2.5 miles)
              2 = PhD Research (breathing space)
              3 = Masters (2-year zones)
              4 = Community Centers
              5 = Private Housing
              6 = Safety Buffer
              7 = Expansion zones
              
seal        : Aura Seal Register
              Cryptographic identity (OBI seal)
              Unique per person/entity
              Used for authentication
```

### 2.4 Policy Registers

```
inv0 - inv7 : Invariant Policy Registers
              Store non-negotiable constitutional policies
              Cannot be overwritten during execution
              
var0 - var7 : Variant Policy Registers
              Store implementation-specific policies
              Can be modified based on context
```

### 2.5 Status Flags Register

```
Bit   Name    Description
───────────────────────────────────────────────────
0     Z       Zero flag
1     N       Negative flag
2     C       Carry flag
3     V       Overflow flag
4     COH     Coherence valid (coh >= 0.954)
5     WIT     Witness logged
6     RING    In valid ring zone
7     GATE    Last gate operation succeeded
```

---

## 3. Instruction Format

### 3.1 Fixed-Width 64-bit Instructions

```
┌──────────┬──────────┬──────────┬──────────┬──────────┐
│  Opcode  │   Dest   │  Src1    │  Src2    │  Flags   │
│  (8-bit) │ (8-bit)  │ (8-bit)  │ (8-bit)  │ (32-bit) │
└──────────┴──────────┴──────────┴──────────┴──────────┘
         64-bit instruction word (fixed width)
```

**Opcode** (8 bits): Operation identifier (256 possible operations)  
**Dest** (8 bits): Destination register  
**Src1** (8 bits): Source register 1  
**Src2** (8 bits): Source register 2 or immediate  
**Flags** (32 bits): Instruction-specific flags and immediate values

### 3.2 Extended Immediate Format

For instructions requiring large immediate values:

```
┌──────────┬──────────┬────────────────────────────────┐
│  Opcode  │   Dest   │    56-bit Immediate Value     │
│  (8-bit) │ (8-bit)  │          (56-bit)             │
└──────────┴──────────┴────────────────────────────────┘
```

---

## 4. Instruction Categories

### 4.1 Data Movement

#### GATE Operations (Human Cognition Model)

```asm
GATE.OPEN  rd, rs            ; rd ← rs (with witness)
GATE.CLOSE rd                ; rd ← 0, log witness
GATE.CHECK rd, rs, cond      ; if cond then rd ← rs
```

#### Classical Load/Store

```asm
LOAD   rd, [addr]            ; rd ← memory[addr]
STORE  rs, [addr]            ; memory[addr] ← rs
LOAD.I rd, imm               ; rd ← immediate value
MOV    rd, rs                ; rd ← rs
```

### 4.2 Arithmetic Operations

```asm
ADD    rd, rs1, rs2          ; rd ← rs1 + rs2
SUB    rd, rs1, rs2          ; rd ← rs1 - rs2
MUL    rd, rs1, rs2          ; rd ← rs1 * rs2
DIV    rd, rs1, rs2          ; rd ← rs1 / rs2
MOD    rd, rs1, rs2          ; rd ← rs1 % rs2
```

### 4.3 Logical Operations

```asm
AND    rd, rs1, rs2          ; rd ← rs1 & rs2
OR     rd, rs1, rs2          ; rd ← rs1 | rs2
XOR    rd, rs1, rs2          ; rd ← rs1 ^ rs2
NOT    rd, rs                ; rd ← ~rs
SHL    rd, rs, shift         ; rd ← rs << shift
SHR    rd, rs, shift         ; rd ← rs >> shift
```

### 4.4 Comparison & Branching

```asm
CMP    rs1, rs2              ; Compare rs1 with rs2 (sets flags)
TEST   rs1, rs2              ; Bitwise test (sets flags)

JUMP   label                 ; Unconditional jump
JUMP.EQ  label               ; Jump if equal (Z=1)
JUMP.NE  label               ; Jump if not equal (Z=0)
JUMP.GT  label               ; Jump if greater than
JUMP.LT  label               ; Jump if less than
JUMP.GTE label               ; Jump if greater or equal
JUMP.LTE label               ; Jump if less or equal
JUMP.IF  rd, label           ; Jump if rd != 0
```

### 4.5 Constitutional Computing (Unique to DSE-ASM)

#### Coherence Operations

```asm
COH.MEASURE rd               ; rd ← current system coherence (0.0-1.0)
COH.ENFORCE threshold        ; Assert coherence >= threshold, trap if fail
COH.RESTORE                  ; Emergency coherence restoration
COH.WITNESS rd, operation    ; Log operation with coherence score
```

#### Observer-Witness Operations

```asm
OBS.INIT agent_id            ; Initialize observer for agent
OBS.WATCH rd, rs             ; rd ← observe(rs), tracks state changes
WIT.LOG operation, data      ; Create witness record in ledger
WIT.VERIFY witness_id        ; Verify witness integrity
WIT.DUMP path                ; Export witness ledger to file
```

#### Invariant/Variant Policy Operations

```asm
INV.LOAD inv_reg, policy_id  ; Load invariant policy into inv_reg
INV.CHECK inv_reg            ; Assert invariant holds, trap if violation
VAR.LOAD var_reg, policy_id  ; Load variant policy into var_reg
VAR.APPLY rd, var_reg, rs    ; Apply variant transformation
VAR.UPDATE var_reg, new_val  ; Update variant policy
```

#### Ring Zone Operations

```asm
RING.ENTER zone_id           ; Enter constitutional ring zone (0-7)
RING.EXIT                    ; Exit current ring zone
RING.CHECK rd, zone_id       ; rd ← (current_ring == zone_id)
RING.ROUTE dest_zone         ; Route to destination zone
DIST.CHECK max_distance      ; Verify distance constraint
```

#### SemVerX Versioning Operations

```asm
SEMVERX.LOAD rd, component   ; Load component version
SEMVERX.PARSE maj, min, pat, ver ; Parse version into parts
SEMVERX.STATE_CHECK rd, ver, state ; Check if version in state
SEMVERX.CAN_HOTSWAP rd, old, new   ; rd ← can_hotswap(old, new)
SEMVERX.HOTSWAP new_version  ; Perform hot-swap to new version
```

#### Geometric Computation Operations

```asm
GEO.MAP rd, sequence, k      ; Map sequence to geometric space
GEO.SPLICE rd, regions       ; splciign: controlled recombination
GEO.VERIFY rd, prototype     ; Verify prototype mapping φ(G)
GEO.CONSTRAINT rd, inc, exc  ; Apply geometric constraints
```

### 4.6 Function Call Operations

```asm
CALL   function              ; Call function (saves PC to lr)
RETURN                       ; Return from function (jump to lr)
PUSH   rs                    ; Push rs onto stack
POP    rd                    ; Pop from stack into rd
```

### 4.7 System Operations

```asm
NOP                          ; No operation
HALT                         ; Stop execution
TRAP   error_code            ; Raise trap/exception
SYSCALL id                   ; System call
```

---

## 5. Addressing Modes

### 5.1 Register Direct
```asm
ADD r1, r2, r3               ; r1 ← r2 + r3
```

### 5.2 Immediate
```asm
LOAD.I r1, 42                ; r1 ← 42
```

### 5.3 Memory Direct
```asm
LOAD r1, [0x1000]            ; r1 ← memory[0x1000]
```

### 5.4 Register Indirect
```asm
LOAD r1, [r2]                ; r1 ← memory[r2]
```

### 5.5 Indexed
```asm
LOAD r1, [r2 + 8]            ; r1 ← memory[r2 + 8]
```

---

## 6. Instruction Encoding Tables

### 6.1 Opcode Assignments

```
Category: Data Movement (0x00 - 0x0F)
─────────────────────────────────────
0x00  NOP
0x01  GATE.OPEN
0x02  GATE.CLOSE
0x03  GATE.CHECK
0x04  LOAD
0x05  STORE
0x06  LOAD.I
0x07  MOV
0x08-0x0F  Reserved

Category: Arithmetic (0x10 - 0x1F)
────────────────────────────────────
0x10  ADD
0x11  SUB
0x12  MUL
0x13  DIV
0x14  MOD
0x15  ADDI  (add immediate)
0x16  SUBI  (subtract immediate)
0x17-0x1F  Reserved

Category: Logical (0x20 - 0x2F)
────────────────────────────────────
0x20  AND
0x21  OR
0x22  XOR
0x23  NOT
0x24  SHL
0x25  SHR
0x26  ROL  (rotate left)
0x27  ROR  (rotate right)
0x28-0x2F  Reserved

Category: Control Flow (0x30 - 0x3F)
────────────────────────────────────
0x30  JUMP
0x31  JUMP.EQ
0x32  JUMP.NE
0x33  JUMP.GT
0x34  JUMP.LT
0x35  JUMP.GTE
0x36  JUMP.LTE
0x37  JUMP.IF
0x38  CMP
0x39  TEST
0x3A  CALL
0x3B  RETURN
0x3C-0x3F  Reserved

Category: Coherence (0x40 - 0x4F)
────────────────────────────────────
0x40  COH.MEASURE
0x41  COH.ENFORCE
0x42  COH.RESTORE
0x43  COH.WITNESS
0x44-0x4F  Reserved

Category: Observer-Witness (0x50 - 0x5F)
────────────────────────────────────
0x50  OBS.INIT
0x51  OBS.WATCH
0x52  WIT.LOG
0x53  WIT.VERIFY
0x54  WIT.DUMP
0x55-0x5F  Reserved

Category: Policy (0x60 - 0x6F)
────────────────────────────────────
0x60  INV.LOAD
0x61  INV.CHECK
0x62  VAR.LOAD
0x63  VAR.APPLY
0x64  VAR.UPDATE
0x65-0x6F  Reserved

Category: Ring Zone (0x70 - 0x7F)
────────────────────────────────────
0x70  RING.ENTER
0x71  RING.EXIT
0x72  RING.CHECK
0x73  RING.ROUTE
0x74  DIST.CHECK
0x75-0x7F  Reserved

Category: SemVerX (0x80 - 0x8F)
────────────────────────────────────
0x80  SEMVERX.LOAD
0x81  SEMVERX.PARSE
0x82  SEMVERX.STATE_CHECK
0x83  SEMVERX.CAN_HOTSWAP
0x84  SEMVERX.HOTSWAP
0x85-0x8F  Reserved

Category: Geometric (0x90 - 0x9F)
────────────────────────────────────
0x90  GEO.MAP
0x91  GEO.SPLICE
0x92  GEO.VERIFY
0x93  GEO.CONSTRAINT
0x94-0x9F  Reserved

Category: Stack (0xA0 - 0xAF)
────────────────────────────────────
0xA0  PUSH
0xA1  POP
0xA2-0xAF  Reserved

Category: System (0xF0 - 0xFF)
────────────────────────────────────
0xF0  HALT
0xF1  TRAP
0xF2  SYSCALL
0xF3-0xFF  Reserved
```

---

## 7. Execution Model

### 7.1 Instruction Pipeline

```
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│  Fetch  │→ │ Decode  │→ │ Execute │→ │ Memory  │→ │Writeback│
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
                                ↓
                          ┌──────────┐
                          │ Coherence│
                          │  Check   │
                          └──────────┘
                                ↓
                          ┌──────────┐
                          │ Witness  │
                          │  Log     │
                          └──────────┘
```

After **every instruction**, the system:
1. Measures coherence: `coh ← measure_coherence()`
2. Checks threshold: If `coh < 0.954`, raises alert
3. Logs witness: Creates witness record in ledger

### 7.2 Trap Handling

When a trap occurs (invariant violation, coherence failure, etc.):

1. Save current state (PC, registers, flags)
2. Log witness record with trap reason
3. Jump to trap handler
4. Trap handler can:
   - Restore coherence
   - Log constitutional violation
   - Generate legal evidence
   - Terminate program

---

## 8. Example Programs

### 8.1 Hello World

```asm
; ═══════════════════════════════════════════════════════
; Hello World in DSE-ASM
; Demonstrates basic I/O and witness logging
; ═══════════════════════════════════════════════════════

.section .data
    hello_msg: .string "Hello, Constitutional World!"

.section .text
.global _start

_start:
    ; Initialize observer
    OBS.INIT "hello_program"
    
    ; Load message address
    LOAD.I r1, hello_msg
    
    ; System call to print
    LOAD.I r0, 1        ; stdout
    LOAD.I r2, 29       ; message length
    SYSCALL 4           ; sys_write
    
    ; Log witness
    WIT.LOG "program_executed", r0
    
    ; Check coherence
    COH.MEASURE coh
    COH.ENFORCE 0.954
    
    ; Exit
    LOAD.I r0, 0        ; exit code
    HALT
```

### 8.2 Housing Entitlement Checker (Full)

See the comprehensive example in Section 3.1 of the main document.

---

## 9. Assembly Syntax

### 9.1 Comments
```asm
; Single-line comment
```

### 9.2 Labels
```asm
function_name:
    ; Instructions
    RETURN

loop_start:
    ; Loop body
    JUMP loop_start
```

### 9.3 Directives

```asm
.section .data          ; Data section
.section .text          ; Code section
.section .invariants    ; Invariant policies
.section .witness       ; Witness records

.global symbol_name     ; Export symbol
.local symbol_name      ; Local symbol

.byte value             ; 8-bit data
.word value             ; 16-bit data
.dword value            ; 32-bit data
.qword value            ; 64-bit data

.string "text"          ; Null-terminated string
.semverx "2.stable.1.experimental.0.legacy"  ; Version

.policy "policy_name"   ; Policy definition
```

---

## 10. Compliance and Verification

Every DSE-ASM program can be formally verified for:

1. **Invariant Policy Adherence**: All `INV.CHECK` operations succeed
2. **Coherence Maintenance**: System never drops below 95.4%
3. **Witness Traceability**: Complete ledger of all operations
4. **Constitutional Compliance**: Ring zone constraints respected

The assembler generates a **compliance certificate** for each program:

```json
{
  "program": "housing_entitlement_checker.dasm",
  "version": "1.0.0",
  "coherence_target": 0.954,
  "invariants_checked": [
    "housing_18_25",
    "meals_min_2_max_5"
  ],
  "ring_zones_accessed": [0, 1, 6],
  "witness_records": 47,
  "verification_status": "PASSED",
  "certificate_hash": "0x..."
}
```

---

**End of ISA Specification**

This specification represents the foundational instruction set for constitutional computing within the OBINexus framework. All instructions are designed to maintain human rights, enforce policies, and provide complete traceability of system behavior.
