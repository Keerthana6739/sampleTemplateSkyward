from django import forms

class AircraftTypeForm(forms.Form):
    name = forms.CharField(max_length=250)
    active = forms.BooleanField(required=False, initial=False)
    

class ServiceLoadForm(forms.Form):
    serviceload_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    service_load_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    service_qty = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    max_children = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    max_infants = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    seat_map = forms.ChoiceField(
        choices=[('', '---select---')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    iata_identifier = forms.ChoiceField(
        choices=[('', '---select---')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class AirCraftForm(forms.Form):
    aircraft_id = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_registration = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_capacity = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_type = forms.ChoiceField(
        choices=[('', 'Select Aircraft Type')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    seatmap = forms.ChoiceField(
        choices=[('', 'Select Seat Map')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    max_cargo_weight = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    calendar_color = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

class SaveRouteForm(forms.Form):
    saveroute_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fromdate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    todate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    miles = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    hours = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    aircraft_type = forms.ChoiceField(
        choices=[('', 'Select Aircraft Type')]  ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class DSTNotificationsForm(forms.Form):
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    dstnotification_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_id = forms.ChoiceField(
        choices=[('', 'Select Aircraft')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    destination = forms.ChoiceField(
        choices=[('', 'Select Destination')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    service_from = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    service_to = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    showon = forms.ChoiceField(
        
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    notification = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    color = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    font_size = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    bold = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    user_availability_screen = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    agents_crs_availability_screen = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    PNR_screen = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    ref_template = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    show_on_seatcontrol = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )

class DSTRestrictForm(forms.Form):
    destination= forms.ChoiceField(
        choices=[('', 'Select Destination')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    dstrestrict_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fromdate = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    todate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    flight_number = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    notification = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )