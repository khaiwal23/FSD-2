import { useState } from "react"; 
import Button from "@mui/material/Button";
import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
// import Grid from "@mui/material/Grid";
import Stack from "@mui/material/Stack";
import Item from "@mui/material/Stack";

export default function LocalStateCounter({ cno }) {
  const [count, setCount] = useState(0);

  // Event handler functions for click Event
  const increaseCount = () => setCount(count + 1);
  const decreaseCount = () => setCount(count - 1);

  return (
    <>
    {/* <Box  sx={{marginBottom:2, '& > button': { m: 1 } }}> */}
      <Container maxWidth="sm">
        <Box sx={{ bgcolor: '#cfe8fc', height: '100px' }} >
          <h3>{cno} : Local State Count: {count}</h3>  
          
          {/* Binding event handlers to buttons  */}
          <Button variant="contained" onClick={increaseCount}>
            Increase
          </Button>
          <Button variant="outlined" onClick={decreaseCount}>
            Decrease
          </Button>
        </Box>           
{/* 
        <Stack spacing={1}>
          <Item>
            <Button variant="contained"  onClick={increaseCount}>
              Increase
            </Button>
          </Item>
          <Item>
            <Button variant="contained" onClick={decreaseCount}>
              Decrease
            </Button>
          </Item>
        </Stack> */}
      </Container>
      
    </>

  );
}