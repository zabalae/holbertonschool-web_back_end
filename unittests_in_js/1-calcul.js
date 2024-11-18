const calculateNumber = (type, a, b) => {
    const numA = Math.round(a);
    const numB = Math.round(b);
  
    if (type === 'SUBTRACT') {
      return numA - numB;
    }
  
    if (type === 'DIVIDE') {
      if (numB === 0) {
        return 'Error';
      }
      return numA / numB;
    }
  
    return numA + numB;
  };
  
  module.exports = calculateNumber;
