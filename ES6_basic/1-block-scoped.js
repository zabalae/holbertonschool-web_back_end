export default function taskBlock(trueOrFalse) {
  // Initialize task variables with default values
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    // Update task variables based on the input parameter
    const task = true;
    const task2 = false;
  }

  return [task, task2];
}
