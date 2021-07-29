from django.shortcuts import render,HttpResponse
import pandas as pd
import math

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Registration number")

def report(request):
    if request.method=='POST':
        opt = request.POST['option']
        if opt not in ['1','2','3','4','5']:
            return HttpResponse("Please choose Valid Option!!!")
        data = pd.read_excel('static/dummy_data.xlsx', sheet_name = 0, index_col = 0)
        df = data.loc[opt]      


        fname = df['First Name'].tolist()[0]
        lname = df['Last Name'].tolist()[0]
        fullName = df['Full Name'].tolist()[0]
        grade = df['Grade'].tolist()[0]
        school = df['Name of School'].tolist()[0]
        dob = df['Date of Birth'].tolist()[0]

        image = f"static/{fullName}.png"  
        round = df['Round'].tolist()[0]
        regNo = df['Registration Number'].tolist()[0]
        gender = df['Gender'].tolist()[0]
        country = df['Country of Residence'].tolist()[0]
        city = df['City of Residence'].tolist()[0]
        marked = df['What you marked'].tolist()
        marked = ['-' if i!=i else i for i in marked]
        questions = []
        for i in range(25):
            questions.append({
                'ques':df['Question No.'].tolist()[i],
                'marked': marked[i],
                'correct':df['Correct Answer'].tolist()[i],
                'outcome':df['Outcome (Correct/Incorrect/Not Attempted)'].tolist()[i],
                'score': df['Score if correct'].tolist()[i],
                'yourScore': df['Your score'].tolist()[i],
            })
        total = sum(df['Your score'].tolist())
        final = df['Final result'].tolist()[0]
        print(image)
        context = {'round': round, 'regNo':regNo, 'gender':gender, 'country':country, 'final':final, 'questions': questions, 'total':total, 'city':city, 'fname':fname, 'lname':lname, 'fullName':fullName, 'school':school, 'grade':grade, 'dob':dob, 'image':image}
        return render(request,'report.html', context)
    return HttpResponse("Server Failed")