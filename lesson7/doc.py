import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage


def get_context(mark, fuel_rate, amount): # возвращает словарь аргуменов
    return {
        'mark': mark,
        'fuel_rate': fuel_rate,
        'amount': amount
    }


def from_template(mark, fuel_rate, amount, template):
    template = DocxTemplate(template)
    context = get_context(mark, fuel_rate, amount)  # gets the context used to render the document


    template.render(context)

    template.save(mark + '_' + str(datetime.datetime.now().date()) + '_report.doc')


def generate_report(mark, fuel_rate, amount):
    template = 'report.doc'
    document = from_template(mark, fuel_rate, amount, template)


def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

generate_report('Volvo', [15.2], '2 500 000')