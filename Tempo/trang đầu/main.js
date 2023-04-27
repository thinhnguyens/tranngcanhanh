body{
    background: url('https://henryz.cc/canvas/tilting-3d-card/img/top-vulture-black.jpg');
    background-size: cover;
    padding: 0;
    margin: 0;
    overflow:hidden;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
}
.card{
    
    height: 360px;
    width: 600px;
    border-radius: 15px;
    box-shadow: -4px 18px 51px -19px rgba(214,185,0,1);
    
}

@media only screen and (max-width: 700px) {
    .card {
        height: 180px;
        width: 300px;
        border-radius: 5px;
    }
  }

/* ref https://blog.logrocket.com/the-noobs-guide-to-3d-transforms-with-css-7370aafd9edf/ */

.scene {    
    perspective: 30em;
  }

