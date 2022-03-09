from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, FormField, FieldList, SelectField,Form

app = Flask(__name__)
app.secret_key = 'simpletest'

class NonValidatingSelectField(SelectField):
    """For some incompatibility the select field seems producing validation error.
    this calss remove the validation.
    """
    def pre_validate(self, form):
        pass 

class Condition(Form):
    """Subform.

    CSRF is disabled for this subform (using `Form` as parent class) because
    it is never used by itself.
    """
    booleanoperator = NonValidatingSelectField(
        'Boolean operator',
        choices=[('and', 'AND'), ('or', 'OR'), ('not', 'NOT')]
    )
    filteroperator = NonValidatingSelectField(
        'Filter',
        choices=[('contains', 'contains'), ('startswith', 'starts with'), ('finish with', 'finish with')]
    )
    searchtext = StringField(
        'Text')

class MainForm(FlaskForm):
    """Parent form."""
    conditions = FieldList(
        FormField(Condition),
        min_entries=0,
        max_entries=20
    )


@app.route('/', methods=['post','get'])
def home():
    form = MainForm()
    template_form = Condition(prefix='conditions-_-')

    if form.validate_on_submit():
        print(form.data)
        #import pdb; pdb.set_trace()
        #return render_template('simple.html', form=form,template_form=template_form)
    print(form.errors)
    return render_template('index_JSnotembedded.html', form=form, template_form=template_form)

if __name__ == '__main__':
    app.run(debug=True)