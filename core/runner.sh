echo "Getting data from files..."
python3 get_data_from_pdf.py

echo "Cleaning data..."
python3 data_cleaner.py

echo "Calculating importance of each and every question..."
python3 sentence_grouping.py

echo "Ranking the questions..."
python3 result_generator.py

echo "Exporting data to pdf..."
python3 export_data_to_pdf.py

echo "Done!"