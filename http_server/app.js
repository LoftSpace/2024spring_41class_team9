const https = require("https");
const path = require("path");
const express = require("express");
require("dotenv").config();

const app = express();

//TODO:job producer에서 id발행, firebase 연동
const userRouter = require("./src/routes/User");

app.use(express.json({
  limit: "32mb"
}));

//Web App and CLI App (user)
app.use("/user", userRouter);

//run
app.listen(8080, () => {
  console.log("running http server");
});
