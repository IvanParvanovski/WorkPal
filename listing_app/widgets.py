from django.forms import Widget
from django.utils.safestring import mark_safe
from django.forms.widgets import Select


class CustomGridSliderWidget(Widget):
    class Media:
        css = {
            'all': ('listing_app/grid_slider.css', ),
        }
        js = ('listing_app/grid_slider.js', )

    def render(self, name, value, attrs=None, renderer=None):
        html = """
        <div class="grid-range-bar">
            <div class="thumb" style="left: 55%;"></div>
            <div class="thumb" style="left: 75%;"></div>
        </div>
        """

        return mark_safe(html)


class SelectWithOtherOptionInputWidget(Select):
    class Media:
        js = ('listing_app/other_input.js',)

    def render(self, name, value, attrs=None, renderer=None):
        select_html = super().render(name, value, attrs={'id': 'selectField'}, renderer=renderer)

        html = """
        <div id="otherInputContainer" style="display: none;">
            <input type="text" id="otherInput" name="other_input" placeholder="Please specify">
        </div>        
        """

        final_html = select_html + html

        return mark_safe(final_html)


widgets = {
    'custom_widget': CustomGridSliderWidget,
    'custom_select': SelectWithOtherOptionInputWidget,
}
