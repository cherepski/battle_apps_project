App = Ember.Application.create();

App.ApplicationRoute = Ember.Route.extend({
  model: function() {
    return Ember.$.getJSON('http://www.bootybattleapp.com/api/v1/profile/1/?format=json');
  }
});
