from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QFormLayout,
    QLabel,
    QSpinBox,
    QDoubleSpinBox,
    QPushButton,
    QCheckBox,
)


class IncomeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Einkommen berechnen")
        self.setFixedSize(400, 300)

        layout = QFormLayout()

        self.hourly_rate_edit = QDoubleSpinBox()
        self.hourly_rate_edit.setRange(0, 999999)
        self.hourly_rate_edit.setDecimals(2)
        layout.addRow(QLabel("Stundenlohn:"), self.hourly_rate_edit)

        self.work_hours_edit = QSpinBox()
        self.work_hours_edit.setRange(0, 9999)
        layout.addRow(QLabel("Arbeitsstunden pro Woche:"), self.work_hours_edit)

        self.weeks_edit = QSpinBox()
        self.weeks_edit.setRange(0, 999)
        layout.addRow(QLabel("Anzahl der Wochen im Jahr:"), self.weeks_edit)

        self.tax_rate_edit = QDoubleSpinBox()
        self.tax_rate_edit.setRange(0, 100)
        self.tax_rate_edit.setSuffix(" %")
        self.tax_rate_edit.setDecimals(2)
        self.tax_rate_edit.setValue(0)
        layout.addRow(QLabel("Steuersatz:"), self.tax_rate_edit)

        self.include_tax_checkbox = QCheckBox("Steuern einbeziehen")
        self.include_tax_checkbox.setChecked(False)
        layout.addRow(self.include_tax_checkbox)

        self.calculate_button = QPushButton("Berechnen")
        self.calculate_button.clicked.connect(self.calculate_income)
        layout.addRow(self.calculate_button)

        self.year_income_label = QLabel()
        layout.addRow(QLabel("Jahreseinkommen:"), self.year_income_label)

        self.month_income_label = QLabel()
        layout.addRow(QLabel("Monatseinkommen:"), self.month_income_label)

        self.week_income_label = QLabel()
        layout.addRow(QLabel("Wocheneinkommen:"), self.week_income_label)

        self.setLayout(layout)

    def calculate_income(self):
        hourly_rate = self.hourly_rate_edit.value()
        work_hours = self.work_hours_edit.value()
        weeks = self.weeks_edit.value()
        tax_rate = self.tax_rate_edit.value() / 100
        include_tax = self.include_tax_checkbox.isChecked()

        yearly_income = hourly_rate * work_hours * weeks
        if include_tax:
            yearly_income = yearly_income * (1 - tax_rate)

        monthly_income = yearly_income / 12
        weekly_income = yearly_income / 52

        self.year_income_label.setText(f"{yearly_income:.2f} EUR")
        self.month_income_label.setText(f"{monthly_income:.2f} EUR")
        self.week_income_label.setText(f"{weekly_income:.2f} EUR")

if __name__ == "__main__":
    app = QApplication([])
    dialog = IncomeDialog()
    dialog.show()
    app.exec_()
