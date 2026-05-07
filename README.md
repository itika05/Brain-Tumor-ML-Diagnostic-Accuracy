# Brain Tumor Diagnostic Accuracy: A Machine Learning Meta-Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)]()

## 📋 Overview

This repository contains a comprehensive **systematic review and meta-analysis** of machine learning models used for brain tumor diagnostic accuracy. The project systematically evaluates various ML approaches including deep learning (CNNs), radiomics, ensemble methods, and classical machine learning algorithms for their diagnostic performance in brain tumor classification.

### Key Features
- 📊 **Comprehensive Meta-Analysis**: Aggregated analysis of multiple studies using ML for brain tumor diagnosis
- 🎯 **Multiple ML Approaches**: Comparison of Deep Learning (CNN), Radiomics, Ensemble, and Classical ML models
- 📈 **Detailed Visualizations**: 10 publication-quality figures including forest plots, SROC curves, and bias assessment
- 🔬 **Rigorous Methodology**: PRISMA and QUADAS-2 standards applied for quality assessment
- 📋 **Structured Data**: Organized data extraction with standardized fields

## 🎯 Objectives

This meta-analysis aims to:
1. **Synthesize evidence** on the diagnostic accuracy of ML models for brain tumors
2. **Compare performance** across different ML techniques and study designs
3. **Evaluate bias** using QUADAS-2 risk assessment methodology
4. **Identify trends** through meta-regression and temporal analysis
5. **Assess publication bias** using funnel plots and trim-fill methods

## 📁 Repository Structure

```
Diagnostic_Accuracy_Machine_Learning/
├── README.md                                    # This file
├── generate_meta_analysis_figures.py           # Main script to regenerate all figures
├── Figures/                                     # Publication-quality visualizations
│   ├── Figure_1_PRISMA_Flow_Diagram.png       # Study selection flow
│   ├── Figure_2_QUADAS2_Risk_of_Bias.png      # Risk of bias assessment
│   ├── Figure_3_Model_Distribution.png         # Distribution of ML approaches
│   ├── Figure_4_Forest_Plot_Overall_Accuracy.png # Overall accuracy meta-analysis
│   ├── Figure_5_Subgroup_Forest_Plots.png     # Subgroup analyses
│   ├── Figure_6_AUC_Forest_and_SROC.png       # AUC forest plot & SROC curve
│   ├── Figure_7_Publication_Bias_Funnel_TrimFill.png # Publication bias assessment
│   ├── Figure_8_MetaRegression_SampleSize_Temporal.png # Trend analyses
│   ├── Figure_9_LeaveOneOut_Sensitivity.png   # Sensitivity analysis
│   └── Figure_10_Summary_Dashboard.png         # Results summary dashboard
├── Supplementary Table Updated_ML_Brain tumors_2026.xlsx  # Data extraction table
└── create_repo.py                              # Repository initialization script
```

## 📊 Key Findings

### Figure Descriptions

| Figure | Description |
|--------|-------------|
| **Figure 1** | PRISMA flow diagram showing study selection process and criteria |
| **Figure 2** | QUADAS-2 risk of bias assessment across included studies |
| **Figure 3** | Distribution and frequency of different ML model types |
| **Figure 4** | Forest plot showing overall pooled diagnostic accuracy |
| **Figure 5** | Subgroup analyses by tumor type, imaging modality, and study design |
| **Figure 6** | AUC forest plot and Summary ROC (SROC) curve |
| **Figure 7** | Publication bias assessment using funnel plot and trim-fill method |
| **Figure 8** | Meta-regression: accuracy trends by sample size and publication year |
| **Figure 9** | Leave-one-out sensitivity analysis assessing study influence |
| **Figure 10** | Summary dashboard presenting all key metrics and outcomes |

## 🔧 Technical Stack

- **Python 3.8+**: Core analysis language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib & Seaborn**: Visualization
- **SciPy**: Statistical analyses
- **Scikit-learn**: Machine learning utilities (if applicable)

## 🚀 Usage

### Prerequisites
```bash
pip install pandas numpy matplotlib seaborn scipy openpyxl
```

### Regenerating Figures
To regenerate all analysis figures from the underlying data:

```bash
python generate_meta_analysis_figures.py
```

This script will:
1. Load the data from the supplementary table (Excel file)
2. Clean and preprocess the data
3. Generate all 10 figures
4. Save them to the `Figures/` directory

## 📖 Data Dictionary

### Key Variables in Data Extraction Table
- **Study Identifiers**: Author, Year, Journal
- **Study Design**: Study type, sample size, imaging modality
- **ML Models**: Algorithm type (CNN, SVM, Random Forest, etc.)
- **Outcomes**: Best Accuracy, Best AUC, Sensitivity, Specificity
- **Tumor Types**: High-grade vs Low-grade gliomas, other brain tumors
- **Quality Metrics**: QUADAS-2 risk of bias assessment

## 📈 Analysis Methods

### Statistical Approaches Used
- **Meta-analysis**: Pooled estimation of diagnostic accuracy
- **Meta-regression**: Exploring heterogeneity sources
- **Publication Bias Assessment**: Funnel plots and trim-fill methods
- **Sensitivity Analysis**: Leave-one-out analysis
- **Subgroup Analysis**: Stratification by tumor type, ML approach, imaging modality

### Quality Assessment
- **QUADAS-2**: Standard tool for diagnostic accuracy bias assessment
- **PRISMA Guidelines**: Systematic review reporting standards

## 🔍 Methodology Highlights

✅ **Systematic Review Protocol**
- Comprehensive literature search across PubMed, Scopus, Web of Science
- Predefined inclusion/exclusion criteria
- Duplicate screening and data extraction

✅ **Machine Learning Categorization**
- Deep Learning (CNNs, ResNets, VGG, Inception, DenseNet)
- Radiomics (texture analysis, hand-crafted features)
- Ensemble Methods (XGBoost, LightGBM, stacking)
- Classical ML (SVM, Random Forest, Decision Trees)

✅ **Tumor Classification**
- High-grade vs Low-grade gliomas
- Grade III vs Grade IV separation
- Specific tumor pathologies (Glioblastoma, etc.)

## 💡 Key Insights

The meta-analysis reveals:
- Deep learning approaches show superior performance in most studies
- Sample size and study design significantly influence reported accuracy
- Publication bias may inflate reported accuracy estimates
- Heterogeneity exists across tumor types and imaging modalities
- Temporal trends show improving ML model performance over time

## 📝 Citation

If you use this meta-analysis in your research, please cite:

```
[Citation information to be added]
```

## 👥 Authors

- **Dritika Arora** - Lead Researcher
- [Team members to be added]

## 📞 Contact & Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Contact the research team

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Yaqin Uddin Lab for research support
- All authors of included studies in the meta-analysis
- Collaborators and reviewers who contributed to study quality

## 📚 Additional Resources

### Related Publications
- PRISMA Guidelines: https://www.prisma-statement.org/
- QUADAS-2 Tool: https://www.birmingham.ac.uk/documents/college-mds/epidemiology/quadas-2.pdf
- Meta-Analysis Methods: [Include relevant methodology papers]

### Brain Tumor Resources
- [National Brain Tumor Society](https://www.braintumor.org/)
- [NIH Brain Tumor Research](https://www.ninds.nih.gov/)

---

**Last Updated**: May 2026
**Version**: 1.0
