# DeepCytokine
A deep learning technique combining Pre-trained Language Models for highly conserved patterns in recognition of cytokine receptor proteins
# Workflow
![Project image](img/DeepCytokine.jpg)
# Quick Start
## Feature Generation
Open a terminal (Linux, MACOS) or cmd (Windows), get access to code folder and run the get_ProtTrans.py:
Ex: python get_ProtTrans.py -in "path/to/your/fasta/files" -out "path/to/your/embeddings"
## Dataset Generation
After retrieving ProtTrans embedings, you can generate a dataset by using get_dataset.py file:
Ex: python get_datatset.py -in "path/to/your/embeddings" -out "path/to/your/file.npy" -dt ".prottrans" -maxseq 500
## Training DeepCytokine
You can train the FASTA files for DeepCytokine model using the quick and easyt-to-follow jupyter notebook: MCNN_Cytokine.pynb
## Test your new data
You can load trained weights and test your new data with aftermcnn.ipynb