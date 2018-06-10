
// Requirements....

var fs = require('fs');
var path = require('path');

var pathOfAssets =  [ __dirname.toString(),  "assets" ].join("/")

var Key = "" ;

function manageAssetsPath(){
    
    window.alert(pathOfAssets)

    if (!fs.existsSync(pathOfAssets)){
        console.log(pathOfAssets)
        fs.mkdirSync(pathOfAssets);
    }
}


function getTargetFlag(){


    return Key;
}

function crack(key , flag , password ){

    Key = key

    manageAssetsPath()

    writeToAssetsFile(password, "password", "txt")
    writeToAssetsFile(flag, "flag", "txt")
    writeToAssetsFile(key, "key", "txt")
 

    launchPythonCommand("python3 binaryconverter.py")
    launchPythonCommand("python3 1pH193N13.py")
}


function writeToAssetsFile(data, filename, extension ){
   
    var file = [pathOfAssets  ,  (filename + "." + extension)].join("/")
    
    fs.writeFileSync(file, data);
 
}; 



