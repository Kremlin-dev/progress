import React, { useState } from 'react';

const SignupForm = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleSignup = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
        credentials: 'include', // Include credentials to allow cookies
      });

      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }

      const data = await response.json();
      console.log(data);

      // After successful signup, retrieve session data
      await getSession();
    } catch (error) {
      console.error('Error signing up:', error);
    }
  };

  const getSession = async () => {
    try {
      const sessionResponse = await fetch('http://localhost:5000/get_session', {
        method: 'GET',
        credentials: 'include', // Include credentials to allow cookies
      });

      if (!sessionResponse.ok) {
        throw new Error(`HTTP error! Status: ${sessionResponse.status}`);
      }

      const sessionData = await sessionResponse.json();
      console.log('Session data:', sessionData);
    } catch (error) {
      console.error('Error getting session:', error);
    }
  };
  return (
    <div>
      <h2>Signup</h2>
      <form>
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </label>
        <br />
        <button type="button" onClick={handleSignup}>
          Sign Up
        </button>
      </form>
    </div>
  );
};

export default SignupForm;
