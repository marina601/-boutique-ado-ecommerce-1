from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """
    A view that renders the bag content page
    """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """
    Add a quantity of the specific product to the bag
    """

    quantity = int(request.POST.get('quantity'))
    # from the form redirect input
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
            else:
                bag[item_id]['items_by_size'][size] = quantity
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
    else:
        """
        Add item to the bag or update the quantity
        if its already exists
        """
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

    """
    Overwrite the variable in the session with
    the updated version
    """
    request.session['bag'] = bag
    return redirect(redirect_url)
