const express = require('express');
const bodyParser = require('body-parser');
const {spawn} = require('child_process');
const ejs = require('ejs');

const app = express();
app.use(bodyParser.urlencoded({extended:true}));
app.use(express.static('public'));
app.set('view engine', 'ejs');

app.get("/",function(req,res){
  res.render("home");
});

app.post("/",function(req,res){
    const python = spawn('python',['gui1.py']);
    var result = "";
    python.stdout.on('data',function(data){
      result+=data.toString();
    });
    python.on('close',function(){
      res.render('result',{result:result});
    })
});

app.post("/upload",function(req,res){
    const python = spawn('python',['gui.py']);
    var result = "";
    python.stdout.on('data',function(data){
      result+=data.toString();
    });
    python.on('close',function(){
      res.render('result',{result:result});
    })
});

app.post('/result',function(req,res){
  res.redirect('/');
});


app.listen('3000',function(){
  console.log("Server is running in port 3000!!!!");
});
