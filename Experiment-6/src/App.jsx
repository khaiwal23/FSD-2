import { TextField, Button, Container, Typography } from '@mui/material';
import { useState } from 'react';

function App() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [errors, setErrors] = useState({});

  const validate = () => {
    let temp = {};
    if(!email.includes('@'))
      temp.email = 'Invalid email';
    if(password.length < 6)
      temp.password = 'Min 6 characters';

    setErrors(temp);
    return Object.keys(temp).length === 0;
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    if(validate())
      alert('Form submitted successfully');
  }

  return (
    <Container maxWidth="sm">
      <Typography variant="h5" gutterBottom>Login Form</Typography>

      <form onSubmit={handleSubmit}>

      <TextField
        fullWidth
        margin="normal"
        label="Email"
        value={email}
        onChange={e => setEmail(e.target.value)}
        error={Boolean(errors.email)}
        helperText={errors.email}
      />

      <TextField
        fullWidth
        margin="normal"
        type="password"
        label="Password"
        value={password}
        onChange={e => setPassword(e.target.value)}
        error={Boolean(errors.password)}
        helperText={errors.password}
      />

      <Button
        variant="contained"
        type="submit"
      >Login</Button>

      </form>
    </Container>
  );
}

export default App;
