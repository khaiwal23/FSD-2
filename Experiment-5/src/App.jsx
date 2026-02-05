import React, { Suspense } from 'react';

const Dashboard = React.lazy(() => import('./Dashboard'));

function App() {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      height: '100vh',
      width: '100vw'
    }}>
      <Suspense fallback={<h3>Loading Dashboard...</h3>}>
        <Dashboard />
      </Suspense>
    </div>
  );
}

export default App;
