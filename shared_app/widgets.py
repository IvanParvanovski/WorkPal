from django.forms import Widget
from django.utils.safestring import mark_safe
from django.forms.widgets import Select


class CustomGridSliderWidget(Widget):
    class Media:
        css = {
            'all': ('widgets/grid_slider.css', ),
        }
        js = ('widgets/grid_slider.js', )

    def render(self, name, value, attrs=None, renderer=None):
        html = """
          <input type="hidden" id="thumb1Position" name="thumb1Position" value="55">
          <input type="hidden" id="thumb2Position" name="thumb2Position" value="75">
          
          <!-- Grid range bar -->
          <div class="grid-range-bar">
              <div class="thumb inner" id="thumb1" style="left: 55%;"></div>
              <div class="thumb outer" id="thumb2" style="left: 75%;"></div>
          </div>
          
          <div class="wages-display">
              <!-- Wages display content goes here -->
              <span class="wage">$8K</span>
              <span class="wage">$31K</span>
              <span class="wage">$57K</span>
              <span class="wage">$82K</span>
              <span class="wage">$108K</span>
              <span class="wage">$132K</span>
              <span class="wage">$151K</span>
              <span class="wage">$185K</span>
          </div>
          
        """

        return mark_safe(html)


class SelectWithOtherOptionInputWidget(Select):
    class Media:
        js = ('widgets/other_input.js',)

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
