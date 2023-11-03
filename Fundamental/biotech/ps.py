# Pipeline Strength of a Pharmaceutical Company
# --------------------------------------------
# Overview:
# The Pipeline Strength metric evaluates the number and potential value of drugs that 
# a company has in different stages of research & development. It gives an idea of the 
# company's future potential and its capability to bring innovative products to the market.
#
# Desired Value:
# Higher values for each stage of R&D indicate a robust pipeline, which can lead to 
# a stronger position in the market upon successful drug launches.
#
# Note: This script takes into account the number of drugs and their potential value 
# at three main R&D stages - Preclinical, Clinical Trials, and Registration.

def pipeline_value(num_drugs, potential_value_per_drug):
    """Calculate the total potential value of drugs at a particular R&D stage."""
    return num_drugs * potential_value_per_drug

# Hard-coded values (expressed in millions where 1 million dollars is 1.00, 10 million is 10.00, etc.)
# Number of drugs at each stage
preclinical_drugs = 5
clinical_trials_drugs = 3
registration_drugs = 1

# Estimated potential value per drug at each stage (in million dollars)
preclinical_value_per_drug = 1.00  
clinical_trials_value_per_drug = 5.00  
registration_value_per_drug = 50.00  

# Calculating total potential value at each stage
preclinical_value = pipeline_value(preclinical_drugs, preclinical_value_per_drug)
clinical_trials_value = pipeline_value(clinical_trials_drugs, clinical_trials_value_per_drug)
registration_value = pipeline_value(registration_drugs, registration_value_per_drug)

# Summing up the values for overall pipeline strength
total_pipeline_strength = preclinical_value + clinical_trials_value + registration_value

print(f"Value from Preclinical Drugs: ${preclinical_value} million")
print(f"Value from Clinical Trials Drugs: ${clinical_trials_value} million")
print(f"Value from Registration Drugs: ${registration_value} million")
print(f"Total Pipeline Strength: ${total_pipeline_strength} million")
