import pandas as pd
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .models import Company, Employee

class UploadFileView(APIView):
    def post(self, request):
        if 'file' not in request.FILES:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        file = request.FILES['file']
        
        if not (file.name.endswith('.xlsx') or file.name.endswith('.csv')):
            return Response({"error": "File format not supported"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Read the file into a DataFrame
            if file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            else:  # file.name.endswith('.csv')
                df = pd.read_csv(file)

            df.columns = df.columns.str.strip().str.lower()

            required_columns = ['first_name', 'last_name', 'phone_number', 'company_name']
            for column in required_columns:
                if column not in df.columns:
                    raise ValidationError(f"Missing required column: {column}")

            companies = {}
            employees = []

            for _, row in df.iterrows():
                company_name = row['company_name']
                if company_name not in companies:
                    company = Company(name=company_name)
                    company.save()
                    companies[company_name] = company

                employees.append(Employee(
                    first_name=row['first_name'],
                    last_name=row['last_name'],
                    phone_number=row['phone_number'],
                    company=companies[company_name]
                ))

            Employee.objects.bulk_create(employees)

            return Response({"message": "Data uploaded successfully"}, status=status.HTTP_201_CREATED)

        except pd.errors.EmptyDataError:
            return Response({"error": "No data found in the file"}, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as ve:
            return Response({"error": str(ve)}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
