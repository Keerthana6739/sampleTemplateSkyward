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
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    aircraft_id = forms.ChoiceField(
        choices=[('', 'Select Aircraft')] ,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    destination = forms.ChoiceField(
        choices=[('', 'Select Destination')] ,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    service_from = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'})
    )
    service_to = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    showon = forms.ChoiceField(
        
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    notification = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    color = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    font_size = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control form-control-sm'})
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
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    dstrestrict_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    fromdate = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'})
    )
    todate = forms.DateField(
        widget=forms.DateInput(attrs={'class': 'form-control form-control-sm', 'type': 'date'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control form-control-sm'})
    )
    flight_number = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )
    notification = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-sm'})
    )

class DSTTimeAddonForm(forms.Form):
    dstaddon_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    destination_id = forms.ChoiceField(
        choices=[('', 'Select Destination')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    flight_number = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    time_add = forms.TimeField(
        widget=forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    fromdate = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    todate = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'})
    )
    add_to = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class AcAvailabilityForm(forms.Form):
    name = forms.CharField(max_length=250)
    active = forms.BooleanField(required=False, initial=False)
    
    ac_number = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    type = forms.ChoiceField(
        choices=[('', 'Select Type')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    date_from = forms.DateField( label="From",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    date_to = forms.DateField( label="To",
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    status = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

class AcAvailabilityTypeForm(forms.Form):
    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    color = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )

class SpecialServicesForm(forms.Form):
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    ss_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_id = forms.ChoiceField(
        choices=[('', 'Select Aircraft')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    block_online_checkin = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    add_to_assistance_list = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    block_ssr_for_mmb = forms.BooleanField( label="Block SSR for MMB",
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    show_on_web = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    order = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    code = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    max_per_flight = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    description = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    detailed_description = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )


class QueuesForm(forms.Form):
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 10px;'})
    )
    queue_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    webhook = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input' , 'style': 'margin-left: 10px;'})
    )
    queue_name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    queue_type = forms.ChoiceField(
      
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    unq = forms.CharField( label="UNQ",
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    agt_id = forms.CharField( label="AGT id",
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    webhook_url = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    status = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )



class DestinationForm(forms.Form):
    order = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    show = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    active = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    destination_id = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    aircraft_id = forms.ChoiceField(
        choices=[('', 'Select Aircraft')] ,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    father = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    show_on_web = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    charge_tax_on_infant = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    block_from_pre_book = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    country = forms.ChoiceField(
        choices=[('', 'Select Country')] ,
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    name = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    code = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    time_zone = forms.ChoiceField(
        choices=[('', 'Select Time Zone')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    lat = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    long = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    father_code = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    allow_strip_change = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    father_destination = forms.ChoiceField(
        choices=[('', 'Select Father Destination')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    crs_color = forms.CharField(
        max_length=250,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    accommodation_mandatory = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    crs_show = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    crs_order = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    baggage_allowance = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    checkin_time_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    online_checkin_open_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    block_online_seat_selection = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    online_checkin_close_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    min_booking_interval_hr = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    min_passenger = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    boarding_time_minutes = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    bar_code_version = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    web_min_booking_interval_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    gate_closing_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    baggage_drop_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    airport_control_min = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    pnl_timing = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    adl_timing = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    adl_continuous = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    pal_timing = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    send_crew_msg = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    use_icao_code_with_flight_number = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    send_pal_cal = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    sita_address_es = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    http_address_es = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    pal_cal_sita_address_es = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    pal_cal_e_mail_s = forms.CharField(
        max_length=250,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    movementtract_email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    template = forms.ChoiceField(
       
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    sightseeing = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )
    return_destination = forms.ChoiceField(
        choices=[('', 'Select Return Destination')],
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
