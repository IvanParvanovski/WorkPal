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
          <input type="hidden" id="thumb1Position" name="thumb1Position" value="55">
          <input type="hidden" id="thumb2Position" name="thumb2Position" value="75">
          
          <!-- Grid range bar -->
          <div class="grid-range-bar">
              <div class="thumb inner" id="thumb1" style="left: 55%;"></div>
              <div class="thumb outer" id="thumb2" style="left: 75%;"></div>
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
