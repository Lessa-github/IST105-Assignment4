# Observation: This view's logic is simplified to match the assignment's example.
from django.shortcuts import render
from .forms import InputForm
import math

def calculator_view(request):
    template_name = 'calculator/result.html'
    context = {} # Start with an empty context
    
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            
            # --- Conditional Logic Starts ---
            # This logic now returns a single error message and stops if any condition fails.
            if a < 1:
                context['error'] = f"Input 'a' ({a}) is less than 1. It must be 1 or greater."
            elif c < 0:
                context['error'] = f"Input 'c' ({c}) is negative. Calculation cannot proceed."
            else:
                # All initial checks passed, proceed with calculation.
                # The 'b == 0' condition is just an observation, so we don't need to show an error for it.
                c_cubed = c ** 3
                
                if c_cubed > 1000:
                    intermediate_result = math.sqrt(c_cubed) * 10
                else:
                    # Check for division by zero, although form validation should prevent a=0.
                    if a == 0:
                         context['error'] = "Error: Value 'a' cannot be zero for this calculation."
                         intermediate_result = None
                    else:
                        intermediate_result = math.sqrt(c_cubed) / a
                
                if 'error' not in context and intermediate_result is not None:
                    final_result = intermediate_result + b
                    context['result'] = final_result
            # --- Conditional Logic Ends ---
        else:
             context['error'] = "Invalid input. Please ensure all values are numeric."
        
        # Always pass the form back to the template, even after submission
        context['form'] = form
        return render(request, template_name, context)

    # For a GET request (the first time the page is loaded), just show the empty form.
    context['form'] = InputForm()
    return render(request, template_name, context)