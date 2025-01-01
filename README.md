### README  

# **Laptop Price Estimator**  

## **Overview**  
The **Laptop Price Estimator** is a Python-based desktop application designed to predict laptop prices based on selected configurations. Built with Tkinter for the GUI and powered by a Random Forest Regressor, this tool offers dynamic dropdown menus for selecting specifications, price estimation in Euros and PKR, and an option to generate an Exploratory Data Analysis (EDA) report for dataset insights.  

---

## **Features**  
- **Price Prediction**: Estimates laptop prices based on specifications such as brand, model, RAM, storage, and processor.  
- **Dynamic Options**: Dropdown menus update automatically based on the selected brand.  
- **Localization**: Converts prices from Euros to Pakistani Rupees (PKR).  
- **EDA Report Generation**: Creates a detailed HTML report of the dataset for further analysis.  
- **User-Friendly Interface**: Clean, intuitive design for easy interaction.  

---

## **Technologies Used**  
- **Programming Language**: Python  
- **Libraries**:  
  - GUI: Tkinter  
  - Machine Learning: Scikit-learn  
  - Data Analysis: Pandas  
  - Profiling: ydata_profiling  

---

## **Requirements**  
- Python 3.8 or higher  
- Required Libraries:  
  ```bash
  pip install pandas scikit-learn ydata-profiling
  ```  

---

## **How to Run the Application**  
1. Clone the repository or download the source code.  
2. Ensure the dataset (`laptop_price.csv`) is placed in the specified directory.  
3. Install the required libraries using the provided command.  
4. Run the script:  
   ```bash
   python laptop_price_estimator.py
   ```  

---

## **Usage**  
1. Select the laptop brand, model, RAM size, storage type, and processor.  
2. Click **"Calculate Price"** to get the estimated price in Euros and PKR.  
3. Click **"Generate EDA Report"** to create a detailed dataset analysis saved as an HTML file.  

---

## **Dataset**  
The application uses a dataset (`laptop_price.csv`) containing laptop specifications and prices. Ensure the dataset is in the correct format with relevant columns for accurate predictions.  

---

## **Future Improvements**  
- Add more specifications for enhanced predictions.  
- Implement a web-based interface for broader accessibility.  
- Expand localization to support other currencies.  

---

## **Contributors**  
- **Developer**: Adeel Sarbazzy  
- **Contact**: [adeelabdulkarim7@gmail.com](mailto:adeelabdulkarim7@gmail.com)  

---

## **License**  
This project is licensed under the MIT License.  

--- 

**Happy Coding!** 🎉
