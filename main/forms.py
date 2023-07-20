from django import forms
from accounts.models import Rate

class rateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = ['GetreadytodoworkRating', 'SkipclassyouwillnotpassRating', 'ClarityRating','TimelyteacherRating','ControlfreakRating','ToughGraderRating','BewareofquestioningRating','LectureheavyRating','NotesprovidedRating','ExtraactivitiesRating']