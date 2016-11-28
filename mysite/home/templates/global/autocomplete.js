$(function() {
  $("#drugs").autocomplete({
    source: "/api/get_drugs/",
    minLength: 2,
  });
});