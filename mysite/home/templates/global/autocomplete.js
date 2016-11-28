$(function() {
  $("input#n").autocomplete({
    source: "{% url autocomplete_recipes %}",
    minLength: 2,
  });
});