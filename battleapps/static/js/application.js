App = Ember.Application.create();

App.ApplicationRoute = Ember.Route.extend({
  model: function() {
    return Ember.$.getJSON('http://www.bootybattleapp.com/api/v1/profile/?format=json');
  }
});

App.jQueryCarouselView = Ember.View.extend({
    didInsertElement: function() {
        $(function() {
            $('.jcarousel_left').jcarousel({
            // Configuration goes here
            });
            $('.jcarousel_right').jcarousel({
            // Configuration goes here
            });
        });
    }
});
