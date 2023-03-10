/* Tab open & color function's */

function openControlPanel() {
    document.getElementById('control-panel').style.visibility = "visible";
    document.getElementById('setting-panel').style.visibility = "hidden";
    document.getElementById('database-panel').style.visibility = "hidden";

    document.getElementById('control-panel__button').style.background = '#f0f0f0';
    document.getElementById('database-panel__button').style.background = 'white';
    document.getElementById('setting-panel__button').style.background = 'white';
};

function openDatabasePanel() {
    document.getElementById('control-panel').style.visibility = "hidden";
    document.getElementById('control-panel').style.position = "absolute";

    document.getElementById('setting-panel').style.visibility = "hidden";
    document.getElementById('setting-panel').style.position = "absolute";

    document.getElementById('database-panel').style.visibility = "visible";

    document.getElementById('database-panel__button').style.background = '#f0f0f0';
    document.getElementById('control-panel__button').style.background = 'white';
    document.getElementById('setting-panel__button').style.background = 'white';
};

function openSettingPanel() {
    document.getElementById('control-panel').style.visibility = "hidden";
    document.getElementById('control-panel').style.position = "absolute";

    document.getElementById('setting-panel').style.visibility = "visible";

    document.getElementById('database-panel').style.position = "absolute";
    document.getElementById('database-panel').style.visibility = "hidden";

    document.getElementById('control-panel__button').style.background = 'white';
    document.getElementById('database-panel__button').style.background = 'white';
    document.getElementById('setting-panel__button').style.background = '#f0f0f0';
};