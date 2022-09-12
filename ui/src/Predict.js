import React from 'react'
import { DropzoneArea } from "material-ui-dropzone";
import { useState } from 'react';
import { Button } from '@mui/material';
import { useEffect } from 'react';
import axios from "axios"
import FormData from 'form-data'
export default function Predict() {
  const proxy = axios.create({
    baseURL:"http://127.0.0.1:5000",
  });
  const PredictStyle={
      width: "30vw"
  };
  const [files, setFiles] = useState(null);
  const [Err, setErr] = useState("");
  const handleChange = (file) => {
        console.log(file);
        setFiles(file);
  };
  const sendFile = ()=>{
    const data = new FormData()
    data.append('file', files)
    const headers ={ "Content-Type": "multipart/form-data" }
    proxy.post('predict',
    data, 
    headers).then((res)=>{
        console.log(JSON.stringify(res))
      }).catch((err)=>{
        
        console.error(err)
        
      })
  }
 
  useEffect(()=>{
      console.log("on mount");
      proxy
      .get("/", proxy)
      .then((res)=>{
        console.log(`res: ${JSON.stringify(res)}`)
        setFiles("");
      })
      .catch((err)=>{
        console.log(`catch ${err}`)
      });
    },
    []
  )
  if(files == null){
    return <>Server is not working!</>
  }
  return (
    <div style={PredictStyle}>
      <DropzoneArea filesLimit={1} acceptedFiles={['image/*']} onChange={(file)=>handleChange(file)}/>
      <Button onClick={()=>sendFile()}>Predict</Button>
      <p style={{color:"red"}}>{Err}</p>
    </div>
  )
}
