# Bacteriocin AlphaFold Models

This repository contains **predicted 3D structures of various bacteriocins** using AlphaFold, generated using the **AlphaFold Google Colab notebook**. Bacteriocins are antimicrobial peptides produced by bacteria and are of significant interest in biotechnology and medicine.

---

## **Project Overview**

- **Objective:** To predict and visualize 3D structures of bacteriocins using AlphaFold (via Colab) for downstream bioinformatics analysis.
- **Scope:** Includes sequences, predicted models, visualizations, and analysis scripts.
- **Applications:** Structural analysis, comparative modeling, potential antimicrobial research.

---

## **Repository Structure**

```
Bacteriocin-alphafold-models/
├── sequences/       # FASTA files for all bacteriocins
├── models/          # AlphaFold predicted 3D structures (.pdb/.cif)
├── images/          # Structure visualizations, ribbon diagrams, plots
├── scripts/         # Python or shell scripts for analysis and automation
└── README.md        # Project overview
```

---

## **Folder Details**

### **1. sequences/**

Contains **FASTA files** of all bacteriocins.  
- Example: `Nisin_Test_a557c.fasta`  

```text
>sp|P13068|Nisin_A|Lactococcus_lactis
MSTKDFNLDLVSVSKKDSGASPRITSISLCTPGCKTGALMGCNMKTATCHCSIHVSK
```

### **2. models/**

Contains **AlphaFold predicted structures** generated via Colab:  
- File formats: `.pdb` or `.cif`  
- Example: `Nisin_Test_a557c.pdb`  

### **3. images/**

Contains **visualizations of predicted structures**, such as:  
- 3D structure images (`.png` / `.jpg`)  
- Ribbon diagrams, topology diagrams  
- Secondary structure plots  

Example files:  
```
Nisin_Test_a557c_structure.png
Nisin_Test_a557c_ribbon.png
```

### **4. scripts/**

Contains **scripts for analysis and automation**, e.g.:  
- `process_sequences.py` – Process FASTA files  
- `plot_structures.py` – Generate plots from structures  
- `run_alphafold.sh` – Automate AlphaFold predictions on Colab  

---

## **How to Use**

1. **Add New Bacteriocins:**
   - Place the FASTA sequence in `sequences/`.  
   - Run AlphaFold via the Colab notebook to generate a `.pdb` file and save in `models/`.  
   - Create visualizations and save in `images/`.

2. **Run Scripts:**
   - Ensure Python dependencies are installed:  
     ```bash
     pip install biopython matplotlib numpy
     ```
   - Run analysis scripts from the `scripts/` folder:  
     ```bash
     python scripts/process_sequences.py
     ```

3. **Visualize Structures:**
   - Open `.pdb` files using PyMOL, ChimeraX, or any 3D viewer.

---

## **Bacteriocins Included**

| Name | UniProt ID | Organism | Sequence Length |
|------|------------|----------|----------------|
| Nisin_A | P13068 | Lactococcus lactis | 57 |
| Pediocin_PA-1 | P29430 | Pediococcus acidilactici | 62 |
| Lacticin3147_A1 | O87236 | Lactococcus lactis | 59 |
| Mersacidin | P43683 | Bacillus sp | 68 |
| Lacticin3147_A2 | O87237 | Lactococcus lactis | 65 |
| Leucocin_A | P34034 | Leuconostoc gelidum | 61 |
| Subtilosin_A | O07623 | Bacillus subtilis | 43 |
| Enterocin_A | C8C4N1 | Enterococcus faecium | 29 |
| Enterocin_JSA | 2M5Z_A | Enterococcus faecalis | 44 |
| Enterocin_P | O30434 | Enterococcus faecium | 71 |
| Plantaricin_A | P80214 | Lactiplantibacillus plantarum | 48 |
| Plantaricin_E | P71470 | Lactiplantaribus plantarum | 56 |

---

## **References**

- [AlphaFold Protein Structure Database](https://www.alphafold.ebi.ac.uk/)  
- UniProt database for sequences: [https://www.uniprot.org](https://www.uniprot.org)  
- Relevant literature on bacteriocins and their applications in biotechnology.
- AlphaFold Colab Notebook: [https://colab.research.google.com/github/deepmind/alphafold](https://colab.research.google.com/github/deepmind/alphafold)

---

## **License**

This repository is available for **research and educational purposes**. Please cite appropriately when using data or models.

---