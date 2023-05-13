import requests
from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from rest_framework import status
import json
@api_view(['GET'])
def home(request):
    return render(request, 'home.html')
@api_view(['GET'])
def flight_selection(request):
    return render(request, 'flight_selection.html')


@api_view(['GET'])
def flight_api(request):
    departure_airport = request.GET.get('departure_airport')
    destin_airport = request.GET.get('destin_airport')
    departure_time = request.GET.get('departure_time')

    flight_api_urls = [
        'http://littleblack.pythonanywhere.com/api/findflight/',
        'http://chentianao.pythonanywhere.com/api/findflight/',
    ]

    all_flights = []

    # 对每个API发送请求
    for url in flight_api_urls:
        response = requests.get(
            url,
            json={
                'dep_airport': departure_airport,
                'dest_airport': destin_airport,
                'dep_date': departure_time,
            },
        )
        if response.status_code == requests.codes.ok:
            flights = response.json()  # flight list
            all_flights.append(flights)
        else:
            return Response({"error": f"Unable to fetch flights from {url}"}, status=status.HTTP_400_BAD_REQUEST)

    return Response(all_flights, status=status.HTTP_200_OK)
'''
    flights=[{'flight_id': '1', 'flight_num': '111', 'dep_airport': 'beijing', 'dest_airport': 'shanghai', 'dep_datetime': 'None', 'arr_datetime': 'None', 'seatbusi_occupied': 111, 'max_seatbusi': 222, 'seatbusi_price': 333.0, 'seatcoom_occupied': 444, 'max_seatcoom': 555, 'seatcoom_price': 666.0, 'seatfirst_occupied': 777, 'max_seatfirst': 888, 'seatfirst_price': 999.0}]
    return JsonResponse({"flights": flights})
'''
@api_view(['GET'])
def create_booking(request):
    return render(request, 'create_booking.html')

@api_view(['POST'])
def create_bookingapi(request):
    flight_number = request.data.get('flight_number')
    passengers = request.data.get('passengers')

    airline_apis = {
        'airline1': 'http://littleblack.pythonanywhere.com/api/bookflight/',
        'airline2': 'http://chentianao.pythonanywhere.com/api/bookflight/',
        'airline3': 'http://127.0.0.1:8000/api/airline3/bookflight/',
        'airline4': 'http://127.0.0.1:8000/api/airline4/bookflight/',
    }

    airline_choice = request.data.get('airline_choice')
    api_url = airline_apis.get(airline_choice)

    if not api_url:
        return Response({"error": "Invalid airline choice"}, status=status.HTTP_400_BAD_REQUEST)

    for passenger in passengers:
        passenger_name = passenger.get('passenger_name')
        passenger_id = passenger.get('passenger_id')
        passenger_phone = passenger.get('passenger_phone')
        seat_type = passenger.get('seat_type')

        response = requests.post(
            api_url,
            json={
                'flight_number': flight_number,
                'passengers': [
                    {
                        'passenger_name': passenger_name,
                        'passenger_id': passenger_id,
                        'passenger_phone': passenger_phone,
                        'seat_type': seat_type
                    }
                ]
            },
        )

        if response.status_code != requests.codes.created:
            return Response({"error": "Unable to create booking for passenger ID: " + passenger_id}, status=status.HTTP_400_BAD_REQUEST)

    booking_id = response.json().get('booking_id')

    return Response({"booking_id": booking_id}, status=status.HTTP_201_CREATED)
'''
    booking=[{
    "booking_id": "BK123456",
    "flight": {
        "flight_id": "FL123456",
        "flight_number": "ABC123",
        "departure_time": "2023-06-01 10:00",
        "arrival_time": "2023-06-01 12:00",
        "departure_airport": "Test Departure Airport",
        "arrival_airport": "Test Arrival Airport",
        "time": "2 hours",
        "seat": [
            {
                "type": "business",
                "price": 200.0,
                "availability": 5
            },
            {
                "type": "common",
                "price": 100.0,
                "availability": 10
            },
            {
                "type": "first",
                "price": 300.0,
                "availability": 3
            }
        ]
    },
    "customer": {
        "customer_id": "CUS123456",
        "name": "John Doe",
        "email": "johndoe@example.com"
    },
    "seat_type": "business",
    "status": "confirmed"
    }]
    return JsonResponse({"booking": booking})
'''

@api_view(['GET'])
def create_refund(request):
    return render(request, 'create_refund.html')

@api_view(['POST'])
def create_refundapi(request):

    booking_id = request.data.get('booking_id')
    passenger_ids = request.data.get('passenger_ids')
    flight_company = request.data.get('flight_company')

    flight_company_apis = {
        'flight1': 'https://api-flight1.com/refunds/',
        'flight2': 'https://api-flight2.com/refunds/',
        'flight3': 'https://api-flight3.com/refunds/',
        'flight4': 'https://api-flight4.com/refunds/'
    }

    refund_data = []
    for passenger_id in passenger_ids:
        response = requests.post(
            flight_company_apis[flight_company],
            json={'booking_id': booking_id, 'passenger_id': passenger_id},
        )

        if response.status_code == requests.codes.created:
            refund = response.json()
            refund_data.append(refund)
        else:
            return Response({"error": "Unable to create refund for customer ID " + passenger_id}, status=status.HTTP_400_BAD_REQUEST)

    return Response(refund_data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def make_payment(request):
    booking_id = request.data.get('booking_id')
    payment_company = request.data.get('payment_company')
    flight_company = request.data.get('flight_company')
    username = request.data.get('username')
    password = request.data.get('password')

    # define the URLs for each payment company API
    payment_login_api = {
        "company1": "https://sc19x2w.pythonanywhere.com/login/",
    }
    payment_company_apis = {
        'company1': 'https://sc19x2w.pythonanywhere.com/pay_order/',
        'company2': 'https://api-company2.com/payments/',
        'company3': 'https://api-company3.com/payments/',
        'company4': 'https://api-company4.com/payments/'
    }
    flight_company_apis = {
        'flight1': 'http://littleblack.pythonanywhere.com/api/payforbooking/',
        'flight2': 'http://chentianao.pythonanywhere.com/api/payforbooking/',
        'flight3': 'https://api-flight3.com/',
        'flight4': 'https://api-flight4.com/'
    }
    flight_comfirm_apis = {
        'flight1': 'http://littleblack.pythonanywhere.com/api/confirm/',
        'flight2': 'http://chentianao.pythonanywhere.com/api/confirm/',
        'flight3': 'https://api-flight3.com/confirm/',
        'flight4': 'https://api-flight4.com/confirm/'
    }

    response = requests.post(
        payment_login_api[payment_company],
        json={
            "username": username,
            'password': password
        }
    )
    token = response.json()["access"]

    response_flight = requests.post(
        flight_company_apis[flight_company],
        json={
            'booking_id': booking_id,
        },

    )

    if response_flight.status_code == requests.codes.ok:
        response_payment = requests.post(
            payment_company_apis[payment_company],
            json=response_flight.json(),

            headers={
                "Authorization": "Bearer " + token  # Assuming your token is a Bearer token
            }
        )

        if response_payment.status_code == requests.codes.created:
            payment = response_payment.json()  # suppose to be an int stamp

            if isinstance(payment, int):
                confirm_api_response = requests.post(
                    flight_comfirm_apis[flight_company],
                    json={'booking_id': booking_id, 'stamp': str(payment)}
                )

                if confirm_api_response.status_code == requests.codes.ok:
                    return Response({"stamp": payment, "message": "Payment successful"}, status=status.HTTP_201_CREATED)
                else:
                    return Response({"error": "Payment successful but failed to send data to Airline"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response({"error": "Payment unsuccessful"}, status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response({"error": "Unable to make payment"}, status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response({"error": "Unable to send booking_id to Airline"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def payment_template(request):
    return render(request, 'make_payment.html')
@api_view(['POST'])
def cancel_booking(request):
    booking_id = request.data.get('booking_id')
    passengers = request.data.get('passengers')
    flight_company = request.data.get('flight_company')  # get flight company

    api_endpoints = {
        'company1': 'http://littleblack.pythonanywhere.com/api/cancelbooking/',
        'company2': 'http://chentianao.pythonanywhere.com/api/cancelbooking/',
    }


    api_endpoint = api_endpoints.get(flight_company)

    if not api_endpoint:
        return Response({"error": "Invalid flight company"}, status=status.HTTP_400_BAD_REQUEST)


    response = requests.post(
        api_endpoint,
        json={'booking_id': booking_id, 'passengers': passengers},
    )

    if response.status_code == 200:  # Check if status code is 200
        return Response({"message": "Booking cancelled successfully"})
    else:
        return Response({"error": "Unable to cancel booking"}, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
def cancel_template(request):
    return render(request, 'cancel_booking.html')

