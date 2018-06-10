var path = require('path');
const ipc = require('electron').ipcRenderer;

var sys = require('sys');
var exec = require('child_process').exec;
var child;

var consoleCtr = 0;
  

document.getElementById("targetFlag").textContent = " Target Flag  is "+ key + "attempts" 

/*
    Overwrite window.log command to print directly to html 
*/

window.console = {
    log: function(str){

      document.getElementById("attackConsole").scrollTop = document.getElementById("attackConsole").scrollHeight;
      document.getElementById("attackConsole").value += str.toString()

      consoleCtr += 1

      document.getElementById("attemptAmmount").textContent= " Iphigenie needed "+ consoleCtr + " attempts"
 
    }
}


 
function launchPythonCommand(cmd) {
  var consoleCtr = 0;
  var nodeConsole = require('console');
  var myConsole = new nodeConsole.Console(process.stdout, process.stderr);
  myConsole.log('\x1b[34m%s\x1b[0m','PRINT BEFORE PYTHON EXEC FROM NODE.JS');

  // EXECUTION OF PYTHON


    // EXECUTION OF PYTHON

    child = exec(cmd , function (error, stdout, stderr) {
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

         
        console.log(data)

    });

}

 