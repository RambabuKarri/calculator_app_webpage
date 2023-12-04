from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import re
# Create your views here.
def greetings(request):
    # var=request.GET['var']
    return render(request,'calc.html')

def calculation(request):
    final_result=None
    if request.method=="POST":
        values=request.POST['values'] #string having whole ques
        print(values)
        vals=re.findall(r"(\d+)",values) #extrect values
        operators=['+','x','÷','-','.','%']
        opr=[]
        for v in values:
            for o in operators:
                if v==o:
                    opr.append(o)
        print(opr)                      #extract operators
        print(re.findall(r"(\d+)",values))

        for o in opr:
            if o=='.':
                i=opr.index(o)
                res=vals[i]+"."+vals[i+1]
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='%':
                i=opr.index(o)
                res=(float(vals[i])/100)*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=res
                print(vals)
                print(opr)
        for o in opr:
            if o=='÷':
                i=opr.index(o)
                res=float(vals[i])/float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='x':
                i=opr.index(o)
                res=float(vals[i])*float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
        for o in opr:
            if o=='+':
                i=opr.index(o)
                res=float(vals[i])+float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
            if o=='-':
                i=opr.index(o)
                res=float(vals[i])-float(vals[i+1])
                vals.remove(vals[i+1])
                opr.remove(opr[i])
                vals[i]=str(res)
                print(vals)
                print(opr)
      
        # print(opr)
        if len(opr)!=0:
            if opr[0]=='÷':
                result = float(vals[0])/float(vals[1])
            elif opr[0]=='x':
                result = float(vals[0])*float(vals[1])
            elif opr[0]=='+':
                result = float(vals[0])+float(vals[1])
            else :
                result = float(vals[0])-float(vals[1])
        else:
            result = float(vals[0])

        final_result=round(result,2)
        print(final_result)
       
    res=render(request,'calc.html',{'result':final_result,'values':values})
    return res

'''
def calculation(request):
    final_result = None
    if request.method == "POST":
        values = request.POST.get('values', '')  # Fetch the string having the entire equation
        print(values)
        
        vals = re.findall(r"(\d+\.?\d*)", values)  # Extract numeric values
        operators = ['+', 'x', '÷', '-', '.', '%']
        opr = re.findall(r"[+\-x÷.%]", values)  # Extract operators
        
        print(vals)
        print(opr)

        # Perform operations considering precedence and left-to-right evaluation
        while '%' in opr:
            idx = opr.index('%')
            res = (float(vals[idx]) / 100) * float(vals[idx + 1])
            vals.pop(idx + 1)
            vals[idx] = str(res)
            opr.pop(idx)
            print(vals)
            print(opr)

        while '÷' in opr:
            idx = opr.index('÷')
            res = float(vals[idx]) / float(vals[idx + 1])
            vals.pop(idx + 1)
            vals[idx] = str(res)
            opr.pop(idx)
            print(vals)
            print(opr)

        while 'x' in opr:
            idx = opr.index('x')
            res = float(vals[idx]) * float(vals[idx + 1])
            vals.pop(idx + 1)
            vals[idx] = str(res)
            opr.pop(idx)
            print(vals)
            print(opr)

        while '.' in opr:
            idx = opr.index('.')
            res = vals[idx] + '.' + vals[idx + 1]
            vals.pop(idx + 1)
            vals[idx] = res
            opr.pop(idx)
            print(vals)
            print(opr)

        while '+' in opr or '-' in opr:
            idx_add = opr.index('+') if '+' in opr else float('inf')
            idx_sub = opr.index('-') if '-' in opr else float('inf')
            idx = min(idx_add, idx_sub)
            
            if idx == float('inf'):
                break
            
            if opr[idx] == '+':
                res = float(vals[idx]) + float(vals[idx + 1])
            else:
                res = float(vals[idx]) - float(vals[idx + 1])

            vals.pop(idx + 1)
            vals[idx] = str(res)
            opr.pop(idx)
            print(vals)
            print(opr)

        if len(opr) != 0:
            if opr[0] == '÷':
                result = float(vals[0]) / float(vals[1])
            elif opr[0] == 'x':
                result = float(vals[0]) * float(vals[1])
            elif opr[0] == '+':
                result = float(vals[0]) + float(vals[1])
            else:
                result = float(vals[0]) - float(vals[1])
        else:
            result = float(vals[0])

        final_result = round(result, 2)
        print(final_result)

    res = render(request, 'calc.html', {'result': final_result, 'values': values})
    return res



def calculation(request):
    final_result = None  # Initialize final_result with a default value

    if request.method == "POST":
        values = request.POST.get('values', '')  # string having whole question
        print(values)

        # ... (rest of your code)

        # Your calculations...

        # Update final_result based on your calculations
        if len(opr) != 0:
            if opr[0] == '÷':
                result = float(vals[0]) / float(vals[1])
            elif opr[0] == 'x':
                result = float(vals[0]) * float(vals[1])
            elif opr[0] == '+':
                result = float(vals[0]) + float(vals[1])
            else:
                result = float(vals[0]) - float(vals[1])
        else:
            result = float(vals[0])

        final_result = round(result, 2)
        print(final_result)

    res = render(request, 'calc.html', {'result': final_result, 'values': values})
    return res
'''