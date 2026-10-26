
def calculate_bmi(height,weight):
    print("Height = ", height)
    print("Weight = ", weight)
    
    bmi=weight / (height*height)
    print("Value of bmi is: ", bmi)
    

    if bmi < 18.5:
      print("BMI is underweight")
    if bmi >=18.5 and bmi <24.9:
        print("BMI is normal weight")
    else:
        print("BMI is overweight")
    return bmi

def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67,32)")
    
def get_user_input():
    txt =input()
    str_list = txt.split(",")
    float_map = map(float, str_list)
    float_list = list(float_map) 
    print(float_list)
    return float_list
    
def calc_average_temperature(temp_list):
    average = sum(temp_list) / len(temp_list)
    return float(average)

def calc_min_max_temperature(temp_list):
    min_temp = int(min(temp_list))
    max_temp = int(max(temp_list))
    return [min_temp, max_temp]

def main():
    print("ET0375 (DevOps for AIOT) - Lab 2 - Introduction in Python")
    display_main_menu()
    num_list=get_user_input()
    bmi_output=calculate_bmi(weight=57,height=1.73)
    print("BMI output is ", bmi_output)
     
    average = calc_average_temperature(num_list)
    print("Average temperature:", average)

    min_max = calc_min_max_temperature(num_list)
    print("Min and Max temperature:", min_max)
    
if __name__ == "__main__":
    main()