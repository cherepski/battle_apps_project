App.BattleImage = DS.Model.extend({
    title: DS.attr('string'),
});

App.BattleImage.FIXTURES = [
    {
        id: 1,
        title: 'Hello, World'
    },
    {
        id: 2,
        title: 'Batttttle'
    }
];
