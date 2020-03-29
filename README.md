# questions_predictor
Predict important and most asked question from a given set of previous year question papers   

# Requirements 
	* TextBlob
    * tqdm
    * json
    * fpdf
    * python image library (PIL)
	* pytesseract
	* pdf2image
    * nltk.corpus (one time download needed for nltk module)  

# Usage  
## For linux systems:
1) First you need to install all the dependencies shown above  

2) Now put all your question paper that are in pdf format to the [training_data](https://github.com/Jonty16117/questions_predictor/tree/master/training_data) folder.  

3) Then just run the [./runner.sh](https://github.com/Jonty16117/questions_predictor/blob/master/core/runner.sh) file in the [core](https://github.com/Jonty16117/questions_predictor/tree/master/core) folder.  

4) Now just collect your final output file from the [results](https://github.com/Jonty16117/questions_predictor/tree/master/results) folder. The output file is in pdf format, therefore it will easy to print the file as well share easiy on other platforms.  

## For windows systems:  
You first need to install WSL(Windows Subsystem for Linux) and then follow the same steps as for linux systems after opening linux shell  

# Note:
The pdf files from which questions are to be analysed can either be scanned pdf (pdf's that contain images) or text pdf's. The program can automatically understand either of them. However any other format is not supported as of now. I will be adding the support for file types such as .doc, txt, jpeg, jpg, png, etc later. But since most of the question papers are in pdf format, most of you will be fine.

# Final note:  
The output of the program will be more helpul if you add as many question papers to the training set. And finally, if you want to score even more marks, then don't use this program :stuck_out_tongue_winking_eye:  

Also feel free to fork, star and contribute [questions_predictor](https://github.com/Jonty16117/questions_predictor) :v: :blush: :v:.





