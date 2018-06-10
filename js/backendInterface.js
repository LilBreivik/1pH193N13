var path = require('path');
const ipc = require('electron').ipcRenderer;

var sys = require('sys');
var exec = require('child_process').exec;
var child;

function launchCracker(flag, password, flag) {
  
    if (evt.srcElement.id == "htmlButtonPress") {
  
      var nodeConsole = require('console');
      var myConsole = new nodeConsole.Console(process.stdout, process.stderr);

      // EXECUTION OF PYTHON
  
      child = exec("python -i pythonExample.py ", function (error, stdout, stderr) {
        //sys.print('stdout: ' + stdout); 
        //sys.print('stderr: ' + stderr); 
        if (error !== null) {
          console.log('exec error: ' + error);
        }
      });
  
      //this is a listener for peers output
      child.stdout.on('data', function(data) {
        var nodeConsole = require('console');
        var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
        myConsole.log('\x1b[36m%s\x1b[0m', 'PIPED FROM PYTHON PROGRAM: ' + data.toString()); 
      });
  
  
  
    }else if(evt.srcElement.id == "interact"){
  
      var nodeConsole = require('console');
      var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
      myConsole.log('\x1b[34m%s\x1b[0m','INTERACTION IN JS');
  
      child.stdin.write("hello\n");
      //this is a listener for peers output
      myConsole.log('\x1b[36m%s\x1b[0m','PIPED FROM PYTHON PROGRAM: ' + data.toString()); 
  
  
    }else{
  
      var nodeConsole = require('console');
      var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
      myConsole.log('\x1b[34m%s\x1b[0m','EXIT IN JS');
  
      child.stdin.write("exit\n");
      //this is a listener for peers output
      myConsole.log('\x1b[36m%s\x1b[0m','PIPED FROM PYTHON PROGRAM: ' + data.toString()); 
  
      child.stdin.end();
      
      var nodeConsole = require('console');
      var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
      myConsole.log('python terminated from js too');
    }
  
  }