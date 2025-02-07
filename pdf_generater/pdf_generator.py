from fpdf import FPDF

class PDFGenerator:
    def create_weekly_meal_pdf(self,user_name, bmi, weekly_plan):
        pdf = FPDF(orientation='P', unit='mm',format='A3')
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()

        # Title
        pdf.set_font("Arial", style='B', size=16)
        pdf.cell(190, 10, f"Weekly Meal Plan for {user_name}", ln=True, align='C')

        # BMI Info
        pdf.set_font("Arial", size=12)
        pdf.cell(190, 10, f"BMI: {bmi}", ln=True, align='C')
        pdf.ln(10)  # Line break

        # Table Header
        pdf.set_font("Arial", style='B', size=12)
        column_widths = [35, 50, 50, 50, 25]  # Adjusted widths for better spacing
        headers = ["Day", "Morning", "Afternoon", "Night", "Total"]
        for i in range(len(headers)):
            pdf.cell(column_widths[i], 10, headers[i], border=1, align='C')
        pdf.ln()

        # Table Data
        pdf.set_font("Arial", size=10)
        total_weekly_calories = 0

        for day, meals in weekly_plan.items():
            morning_meal, morning_cal = meals["Morning"]
            afternoon_meal, afternoon_cal = meals["Afternoon"]
            night_meal, night_cal = meals["Night"]

            daily_total = morning_cal + afternoon_cal + night_cal
            total_weekly_calories += daily_total

            pdf.cell(column_widths[0], 10, day, border=1, align='C')
            pdf.cell(column_widths[1], 10, f"{morning_meal} ({morning_cal}C)", border=1, align='C')
            pdf.cell(column_widths[2], 10, f"{afternoon_meal} ({afternoon_cal}C)", border=1, align='C')
            pdf.cell(column_widths[3], 10, f"{night_meal} ({night_cal}C)", border=1, align='C')
            pdf.cell(column_widths[4], 10, f"{daily_total}C", border=1, align='C')
            pdf.ln()

        # Total Weekly Calories Row
        pdf.set_font("Arial", style='B', size=12)
        pdf.cell(sum(column_widths[:-1]), 10, "Total Weekly Calories:", border=1, align='R')
        pdf.cell(column_widths[-1], 10, f"{total_weekly_calories}C", border=1, align='C')

        # Save PDF
        pdf.output("weekly_meal_plan.pdf")
        print("PDF Generated: weekly_meal_plan.pdf")

# Example Data
weekly_plan = {
    "Monday":    {"Morning": ("Oats", 300), "Afternoon": ("Rice & Chicken", 600), "Night": ("Salad", 200)},
    "Tuesday":   {"Morning": ("Fruits", 250), "Afternoon": ("Pasta", 550), "Night": ("Soup", 250)},
    "Wednesday": {"Morning": ("Eggs", 200), "Afternoon": ("Fish & Rice", 650), "Night": ("Vegetables", 180)},
    "Thursday":  {"Morning": ("Smoothie", 180), "Afternoon": ("Chicken Salad", 500), "Night": ("Soup", 250)},
    "Friday":    {"Morning": ("Pancakes", 250), "Afternoon": ("Grilled Fish", 600), "Night": ("Dal & Rice", 400)},
    "Saturday":  {"Morning": ("Omelet", 220), "Afternoon": ("Veggie Wrap", 500), "Night": ("Paneer Curry", 350)},
    "Sunday":    {"Morning": ("Toast", 180), "Afternoon": ("Biryani", 700), "Night": ("Yogurt & Fruits", 300)},
}

pdf = PDFGenerator()
pdf.create_weekly_meal_pdf("John Doe", 22.5, weekly_plan)
