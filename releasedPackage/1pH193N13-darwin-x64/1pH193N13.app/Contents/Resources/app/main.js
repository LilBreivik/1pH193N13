const {app, BrowserWindow} = require('electron');
const ipc = require('electron').ipcMain;

app.on('window-all-closed', () => {
  app.quit()
})

app.on('ready', () => {

	var ui = new BrowserWindow({
		titleBarStyle: 'hidden' ,
		height: 850,
		width: 800,
		resizable: true, 
		icon: 'file://' + __dirname + 'icons/pepe/64x64.png'

	});
	
	
	ui.loadURL('file://' + __dirname + '/attackconsole.html');
	
	ui.on('closed', () => {
  		app.quit()
	})

	ipc.on('openJsonFile', () => { 
		
		var fs = require('fs');
		var fileName = './config.json';
		var file = require(fileName);
 
		
	});

});
 