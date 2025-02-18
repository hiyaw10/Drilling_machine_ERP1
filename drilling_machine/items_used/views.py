from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ItemsUsedForm
from .models import ItemsUsed  # Import the ItemsUsed model
from purchase.forms import ItemForm



def add_items_used(request):
    if request.method == 'POST':
        form = ItemsUsedForm(request.POST)
        if form.is_valid():
            try:
                # Save the form without committing to the database
                item_used = form.save(commit=False)
                
                # Save the item usage record
                item_used.save()
                return redirect('inventory:inventory_list')
                # Success message
                messages.success(request, "Item usage recorded successfully!")
                
                # Redirect to the inventory list
                return redirect('inventory:inventory_list')
            except ValueError as e:
                # Handle the error for not enough stock
                messages.error(request, str(e))
            except Exception as e:
                # Catch any other exception
                messages.error(request, f"Error: {str(e)}")
    else:
        form = ItemsUsedForm()

    return render(request, 'items_used/add_items_used.html', {'form': form})


def items_used_report(request):
    """Displays a permanent log of all items used."""
    items_used = ItemsUsed.objects.all().order_by('-date_of_use')  # Keep a history sorted by date
    return render(request, 'items_used/items_used_report.html', {'items_used': items_used})

