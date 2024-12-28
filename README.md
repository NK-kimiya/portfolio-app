<h3 align="center">summary</h3>

Enter a text summary of the application or service you wish to create.
Predicts the label class from the received text and returns the location of the git hub repository that will serve as the template.


https://github.com/user-attachments/assets/5992cda1-7653-4e2e-b67a-320d0e2a8bcd



<h4>platform</h4>
Anaconda Navigator

<h4>Main Tools</h4>
<ul>
  <li>python</li>
  <li>Django</li>
  <li>PyTorch</li>
</ul>

<h4>pre-trained model</h4>

BertForSequenceClassification

<h3 align="center">Usage Procedure</h4>
<h4>1：Installing packages</h4>
<p>Install the packages listed in requirements.txt</p>

<p>command：pip install -r requirements.txt</p>

<h4>2: Database Migration</h4>

<p>command：cd project_search_system</p>
<p>command：python manage.py migrate</p>

<h4>3:Server startup</h4>
<p>command：python manage.py runserver</p>

<h3 align="center">Data Learning</h3>

<h4>Installing the NVIDIA GPU Computing Toolkit (CUDA Toolkit)</h4>
<p>https://developer.nvidia.com/cuda-downloads</p>

<h4>Installing packages</h4>
<p>command：pip install -r requirements.txt</p>

<h4>supplementary information</h4>
<p>Check CUDA version and install CUDA-compatible PyTorch according to the version.</p>
<p>command：nvcc --version</p>
<p>command：pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu126</p>
<small>(Verify command　https://pytorch.org/get-started/locally/)</small>
　

<h3>Data Preparation</h3>
<p>1:Writes data from a csv file to a text file</p>
<p>executable filez:text_file_generation.ipynb</p>

<p>2:Fine-tuning is performed with the prepared text file and the model is saved in the model_transformers folder.</p>
<p>executable file:data_learning.ipynb</p>

<h5>Usage environment</h5>
<ul>
  <li>OS：Windows11</li>
  <li>CPU：Core i7</li>
  <li>RAM：8GB</li>
  <li>GPU：NVIDIA GeForce RTX 3060 Ti</li>
</ul>
