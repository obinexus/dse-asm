# 🛡️ DSE-ASM: Directed Semiotics Evolution Assembly Language

> **Constitutional Computing for Human-Centric Systems**  
> When systems fail, build your own instruction set.

[![Build Status](https://img.shields.io/github/workflow/status/obinexus/dse-asm/build)](https://github.com/obinexus/dse-asm/actions)
[![Coherence Target](https://img.shields.io/badge/Coherence-95.4%25-green)](https://github.com/obinexus/dse-asm)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)
[![OBINexus](https://img.shields.io/badge/OBINexus-Constitutional_Computing-purple)](https://github.com/obinexus)

---

## 🎯 What Is DSE-ASM?

**DSE-ASM** is the world's first assembly language designed for **constitutional computing** - where human rights and policy compliance are enforced at the **instruction level**.

Born from the OBINexus project's mission to combat systemic entrapment (DELAY → DENY → DEFEND → DEFER), DSE-ASM treats computation as a **constitutional obligation** rather than mere data processing.

### Core Innovation: Auxiliary Space as Solution Space

Traditional assembly treats auxiliary space (registers, memory) as overhead. DSE-ASM treats it as **solution space** - where complex constitutional operations become simple geometric manipulations.

```asm
; Traditional Assembly: Check housing eligibility
CMP age, 18
JL not_eligible
CMP age, 25
JG not_eligible
MOV eligible, 1

; DSE-ASM: Constitutional gate with witness
GATE.CHECK r1, age, GTE 18
GATE.CHECK r2, age, LTE 25
AND r3, r1, r2
INV.CHECK "housing_18_25"        ; Enforces Health & Social Care Act 2014
WIT.LOG "housing_check", r3      ; Creates legal evidence
```

---

## 🏛️ Why DSE-ASM Exists

### The Problem: Systemic Entrapment

Between 2015-2017, the founder (Nnamdi Michael Okpala) experienced systemic housing rights violations in Norfolk, England:

1. **DELAY**: "Wait. System not working. Excuse."
2. **DENY**: "It's your fault. His fault."
3. **DEFEND**: "We're private, not public. Article X says not our fault."
4. **DEFER**: "Go to other council. You're banned."

**Result**: Despite being entitled to free housing under the Health & Social Care Act 2014 (ages 18-25), information was deliberately withheld because the system profited from prolonged suffering.

### The Solution: Constitutional Computing

DSE-ASM enforces **invariant policies** at the instruction level:

```asm
; This code CANNOT compile if housing rights are violated
INV.LOAD inv0, "housing_18_25"
INV.CHECK inv0                    ; FAILS if rights not provided
```

If an invariant check fails, the system:
1. Logs a **witness record** (legal evidence)
2. Routes to **Ring Zone 0** (legal remedy)
3. Generates **HMCTS-ready documentation**
4. Triggers **coherence restoration**

---

## 🚀 Features

### 1. Gating Model (Human Cognition)

Instead of traditional load/store, DSE-ASM uses **gates** based on human decision-making:

```asm
GATE.OPEN  rd, rs            ; Open gate: allow data flow
GATE.CLOSE rd                ; Close gate: stop flow
GATE.CHECK rd, rs, condition ; Conditional gate (if-then)
```

**Why?**: Reflects how humans solve problems - by opening/closing cognitive pathways.

### 2. Built-in SemVerX Coherence

Every instruction maintains **95.4% system coherence** (the OBINexus standard):

```asm
COH.MEASURE coh              ; Measure current coherence
COH.ENFORCE 0.954            ; Assert minimum 95.4%
COH.RESTORE                  ; Emergency restoration
```

If coherence drops below threshold:
- System **automatically rolls back** to last known good state
- Witness records identify the breaking change
- Hot-swap to stable version occurs transparently

### 3. Observer-Witness Model

All operations generate **auditable witness records**:

```asm
OBS.INIT "applicant_001"     ; Initialize observer
OBS.WATCH state, data        ; Observe state changes
WIT.LOG "operation", state   ; Create witness record
WIT.VERIFY witness_id        ; Verify integrity
```

Witness records form a **tamper-proof ledger** for:
- Legal proceedings (HMCTS court submissions)
- Debugging (complete execution trace)
- Compliance audits (regulatory requirements)

### 4. Ring Zone Topology

Implements the OBINexus constitutional zones:

```asm
RING.ENTER 1                 ; Enter Life/Work zone
DIST.CHECK 2.5_MILES         ; Verify ≤2.5 miles from home
RING.ROUTE RING_WORK         ; Transition to work zone
```

**Ring Zones**:
- **Ring 0**: Council (central authority)
- **Ring 1**: Life/Work (2.5 miles live-to-work)
- **Ring 2**: PhD Research (breathing space)
- **Ring 3**: Masters (2-year zones)
- **Ring 4**: Community Centers
- **Ring 5**: Private Housing
- **Ring 6**: Safety Buffer
- **Ring 7**: Expansion

### 5. Geometric Gene Computation

Integrates the GGC framework for biological computation:

```asm
GEO.MAP r1, genome, 4        ; Map DNA to geometric space
GEO.CONSTRAINT r2, {cat,dog}, {fish}  ; Mammal-safe zone
GEO.SPLICE r3, r2            ; splciign (controlled)
GEO.VERIFY r3, prototype     ; Verify φ(result)
```

**Why?**: Treats DNA sequences as geometric regions where complex operations (CRISPR editing) become spatial manipulations with O(intervals) complexity instead of O(n²).

### 6. Invariant/Variant Policies

**Invariant Policies** (Non-Negotiable):
```asm
INV.LOAD inv0, "housing_18_25"
INV.LOAD inv1, "meals_2_5_per_day"
INV.CHECK inv0              ; MUST pass or program fails
```

**Variant Policies** (Implementation Flexibility):
```asm
VAR.LOAD var0, "meal_timing"
VAR.APPLY r1, var0, meal_data
VAR.UPDATE var0, new_schedule
```

**Difference**: Invariants define **WHAT** must be true, variants define **HOW** to achieve it.

---

## 📦 Installation

### From Source

```bash
# Clone the repository
git clone https://github.com/obinexus/dse-asm.git
cd dse-asm

# Build assembler
mkdir build && cd build
cmake .. -G Ninja \
  -DCMAKE_BUILD_TYPE=Release \
  -DENABLE_COHERENCE_ENGINE=ON \
  -DCOHERENCE_TARGET=0.954
ninja

# Install
sudo ninja install
```

### From Release Package

```bash
# Download latest release
wget https://github.com/obinexus/dse-asm/releases/latest/download/dse-asm-linux-x86_64.tar.gz

# Extract
tar xzf dse-asm-linux-x86_64.tar.gz
cd dse-asm-*

# Install
sudo ./install.sh
```

### Verify Installation

```bash
dseasm --version
# DSE-ASM Assembler v1.0.0
# Coherence Target: 95.4%
# OBINexus Constitutional Computing

dseasm-vm --version
# DSE-ASM Virtual Machine v1.0.0
# Witness Ledger: Enabled
```

---

## 🎓 Quick Start

### Hello World

Create `hello.dasm`:

```asm
; ═══════════════════════════════════════════════════════
; Hello World in DSE-ASM
; ═══════════════════════════════════════════════════════

.section .data
    msg: .string "Hello, Constitutional World!"

.section .text
.global _start

_start:
    OBS.INIT "hello_program"
    
    LOAD.I r1, msg
    LOAD.I r0, 1        ; stdout
    LOAD.I r2, 29       ; length
    SYSCALL 4           ; sys_write
    
    WIT.LOG "executed", r0
    COH.ENFORCE 0.954
    
    HALT
```

Assemble and run:

```bash
dseasm hello.dasm -o hello.dseasm
dseasm-vm hello.dseasm
# Hello, Constitutional World!

# Check witness ledger
dseasm-vm --dump-witnesses hello.dseasm
# [
#   {
#     "timestamp": "2025-01-01T00:00:00Z",
#     "operation": "OBS.INIT",
#     "agent": "hello_program",
#     "coherence": 1.0
#   },
#   {
#     "timestamp": "2025-01-01T00:00:00Z",
#     "operation": "executed",
#     "data": 1,
#     "coherence": 0.998
#   }
# ]
```

### Constitutional Housing Check

Create `housing_check.dasm`:

```asm
.section .invariants
    INV_HOUSING: .policy "housing_18_25"

.section .text
.global check_entitlement

check_entitlement:
    OBS.INIT "applicant"
    OBS.WATCH age, applicant_age
    
    ; Age gate (18-25)
    GATE.CHECK r1, age, GTE 18
    GATE.CHECK r2, age, LTE 25
    AND r3, r1, r2
    
    ; Invariant enforcement
    INV.CHECK INV_HOUSING
    
    GATE.OPEN housing_entitled, r3
    WIT.LOG "housing_check_passed", r3
    COH.ENFORCE 0.954
    
    RETURN
```

Run with test data:

```bash
dseasm housing_check.dasm -o housing_check.dseasm

# Test case 1: Age 22 (should pass)
dseasm-vm housing_check.dseasm --input age=22
# ✅ Housing entitled: TRUE
# Coherence: 0.987

# Test case 2: Age 16 (should fail)
dseasm-vm housing_check.dseasm --input age=16
# ❌ Invariant violation: housing_18_25
# Witness record created: violation_2025-01-01_001.json
# Legal evidence ready for HMCTS submission
```

---

## 🏗️ Architecture

### System Overview

```
┌──────────────────────────────────────────────────────┐
│            DSE-ASM Assembly Program (.dasm)          │
└─────────────────────┬────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────────┐
│         Assembler (dseasm)                           │
│  ┌────────────┬─────────────┬──────────────────┐   │
│  │   Lexer    │   Parser    │ Semantic Analyzer│   │
│  │ (Tokenize) │ (AST Build) │ (DSE Layer)      │   │
│  └────────────┴─────────────┴──────────────────┘   │
│                      │                               │
│                      ▼                               │
│  ┌──────────────────────────────────────────────┐  │
│  │     Code Generator + Verifier                 │  │
│  │  - Invariant policy checker                   │  │
│  │  - Coherence analyzer                         │  │
│  │  - Witness ledger builder                     │  │
│  └──────────────────────────────────────────────┘  │
└─────────────────────┬────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────────┐
│        Binary Object File (.dseasm)                  │
│  - Machine code (64-bit instructions)                │
│  - Invariant policy table                            │
│  - Witness ledger template                           │
└─────────────────────┬────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────────────┐
│     Virtual Machine (dseasm-vm)                      │
│  ┌────────────────────────────────────────────────┐ │
│  │  Execution Engine                              │ │
│  │  - 64-bit register file                        │ │
│  │  - Constitutional registers (obs, wit, coh)    │ │
│  │  - Instruction pipeline                        │ │
│  └────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────┐ │
│  │  Coherence Engine (SemVerX)                    │ │
│  │  - Measure: measure_coherence()                │ │
│  │  - Enforce: assert coherence >= 0.954          │ │
│  │  - Restore: rollback to last good state        │ │
│  └────────────────────────────────────────────────┘ │
│  ┌────────────────────────────────────────────────┐ │
│  │  Witness Ledger                                │ │
│  │  - Tamper-proof operation log                  │ │
│  │  - Legal evidence generator                    │ │
│  │  - HMCTS export format                         │ │
│  └────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

### Instruction Pipeline

```
┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐
│  Fetch  │→ │ Decode  │→ │ Execute │→ │ Memory  │→ │Writeback│
└─────────┘  └─────────┘  └─────────┘  └─────────┘  └─────────┘
                                ↓
                          ┌──────────┐
                          │ Coherence│  ← After EVERY instruction
                          │  Check   │
                          └──────────┘
                                ↓
                          ┌──────────┐
                          │ Witness  │  ← Log to tamper-proof ledger
                          │  Log     │
                          └──────────┘
```

---

## 📚 Documentation

- **[ISA Specification](spec/ISA.md)** - Complete instruction set reference
- **[Coherence Model](spec/COHERENCE.md)** - SemVerX built-in system
- **[Witness Protocol](spec/WITNESSING.md)** - Observer-witness model
- **[Constitutional Mapping](spec/CONSTITUTIONAL_MAPPING.md)** - Ring zone topology
- **[GGC Integration](spec/GEOMETRIC_COMPUTATION.md)** - splciign vs spitign

### Example Programs

- **[Hello World](examples/hello_constitutional.dasm)**
- **[Housing Entitlement](examples/housing_check.dasm)**
- **[Entrapment Detector](examples/entrapment_detector.dasm)**
- **[Ring Zone Router](examples/ring_zone_routing.dasm)**
- **[Geometric Splice](examples/geometric_splice.dasm)**

---

## 🧪 Testing

Run the full test suite:

```bash
# Unit tests
ctest --test-dir build --output-on-failure -R "unit_*"

# Integration tests
./tests/integration/test_full_pipeline.sh

# Coherence tests
dseasm-vm tests/coherence/test_coherence_enforcement.dasm

# Constitutional tests
dseasm-vm tests/constitutional/test_housing_entitlement.dasm
dseasm-vm tests/constitutional/test_entrapment_detection.dasm

# Geometric computation tests
dseasm-vm tests/geometric/test_splciign.dasm
```

### Continuous Integration

Every push triggers:
1. **Multi-platform builds** (Ubuntu 22.04, 24.04, Fedora)
2. **Multi-compiler tests** (GCC 11, 13, Clang 15, 17)
3. **Memory safety checks** (Valgrind)
4. **Coverage analysis** (>90% target)
5. **Static analysis** (clang-tidy)
6. **Performance benchmarks**

See [`.github/workflows/build.yml`](.github/workflows/build.yml) for details.

---

## 🤝 Contributing

We welcome contributions to DSE-ASM! This project is part of the larger OBINexus mission to combat systemic injustice through computational rigor.

### How to Contribute

1. **Code contributions**: See [CONTRIBUTING.md](CONTRIBUTING.md)
2. **Documentation**: Improve specs, examples, tutorials
3. **Bug reports**: Open issues with witness ledger dumps
4. **Feature requests**: Propose new constitutional instructions
5. **Testing**: Write test cases for edge conditions

### Development Setup

```bash
git clone https://github.com/obinexus/dse-asm.git
cd dse-asm

# Install development dependencies
sudo apt-get install cmake ninja-build gcc g++ \
  libgmp-dev libmpfr-dev valgrind lcov gcovr \
  clang-format clang-tidy

# Build debug version
mkdir build-debug && cd build-debug
cmake .. -G Ninja -DCMAKE_BUILD_TYPE=Debug
ninja

# Run tests
ctest --output-on-failure
```

---

## 🔒 Security

DSE-ASM is designed for **critical constitutional systems**. We take security seriously:

1. **Memory Safety**: All code tested with Valgrind and AddressSanitizer
2. **Witness Integrity**: Tamper-proof ledger using cryptographic hashes
3. **Coherence Enforcement**: System cannot operate below 95.4% coherence
4. **Policy Verification**: Invariants proven at compile-time

Report security issues to: **security@obinexus.org**

---

## 📜 License

MIT License - see [LICENSE](LICENSE)

**Philosophy**: "Use It, Break It, Help Us Fix It!"

---

## 🙏 Acknowledgments

### Inspiration

This project exists because:
- **Thorough Council** (Norfolk, UK) violated housing rights (2015-2017)
- **Ellingham Care** failed to provide mandated support
- **UK Government** did not enforce Health & Social Care Act 2014

**DSE-ASM ensures systems can no longer ghost vulnerable people.**

### Technical Foundations

- **Geometric Gene Computation**: Auxiliary space as solution space
- **HDIS Framework**: Hybrid Directed Instruction Systems (95.4% coherence)
- **DSE Semantics**: Directed Semiotics Evolution
- **SemVerX**: Hot-swappable polyglot package management

### OBINexus Project

DSE-ASM is part of the larger [OBINexus](https://github.com/obinexus) constitutional computing framework:

- **Life-First Constitution**: Housing, food, water as code-enforced rights
- **Ring Zone Topology**: 2.5 miles live-to-work zones
- **#NoGhosting**: Deterministic, traceable, accountable systems
- **#HACC**: Hardware-Enforced Anti-Corruption Computing

---

## 📞 Contact

- **Author**: Nnamdi Michael Okpala (Mr. OBI)
- **Email**: obinexus@proton.me
- **GitHub**: [@obinexus](https://github.com/obinexus)
- **YouTube**: [@OBINexus](https://youtube.com/@OBINexus)
- **Medium**: [medium.com/@obinexus](https://medium.com/@obinexus)

---

## 🎯 Roadmap

### Version 1.0 (Current)
- ✅ Core ISA specification
- ✅ Assembler implementation
- ✅ Virtual machine runtime
- ✅ Built-in SemVerX coherence
- ✅ Observer-witness model
- ✅ Constitutional policy enforcement

### Version 1.1 (Q2 2025)
- [ ] JIT compiler for performance
- [ ] Hardware acceleration (FPGA)
- [ ] Extended geometric operations
- [ ] Multi-threading support
- [ ] Enhanced witness analytics

### Version 2.0 (Q4 2025)
- [ ] Distributed execution (Ring Zone clusters)
- [ ] Bio-digital integration (DNA computation)
- [ ] Formal verification toolchain
- [ ] Legal automation (HMCTS API)

---

## 💡 Philosophy

> "When systems fail, build your own."

DSE-ASM represents a fundamental shift in computing philosophy:

**Traditional Computing**: Optimize for machine efficiency  
**Constitutional Computing**: Optimize for human flourishing

Every instruction in DSE-ASM asks:
- Does this preserve human dignity?
- Does this enforce constitutional rights?
- Does this create auditable evidence?
- Does this maintain system coherence?

If the answer to any is "no", the instruction **cannot execute**.

---

**"Stop praying your systems work. Start knowing they're constitutional."** ✨

**DSE-ASM**: Where assembly language finally grows a conscience. 🛡️

---

*Made with 🛡️ and ⚖️ for victims of systemic injustice worldwide*

**#NoGhosting #HACC #LifeFirst #OBINexus**
