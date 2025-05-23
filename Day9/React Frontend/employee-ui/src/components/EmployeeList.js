import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { Button, Table, TableHead, TableRow, TableCell, TableBody } from '@mui/material';

export default function EmployeeList() {
  const [employees, setEmployees] = useState([]);

  const fetchEmployees = async () => {
    const res = await axios.get('http://localhost:8000/api/employees/');
    setEmployees(res.data);
  };

  const deleteEmployee = async (id) => {
    await axios.delete(`http://localhost:8000/api/employees/${id}/`);
    fetchEmployees();
  };

  useEffect(() => {
    fetchEmployees();
  }, []);

  return (
    <div>
      <h2>Employee List</h2>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Name</TableCell>
            <TableCell>Department</TableCell>
            <TableCell>Salary</TableCell>
            <TableCell>Actions</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {employees.map(emp => (
            <TableRow key={emp.id}>
              <TableCell>{emp.name}</TableCell>
              <TableCell>{emp.department}</TableCell>
              <TableCell>{emp.salary}</TableCell>
              <TableCell>
                <Button onClick={() => deleteEmployee(emp.id)} color="error">Delete</Button>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  );
}
