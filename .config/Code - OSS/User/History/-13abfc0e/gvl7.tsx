import React from "react";

export default function Table() {
  return (
    <div>
      <table>
        <thead>
          <tr>
            <th>Full name</th>
            <th>Email</th>
            <th>Address</th>
            <th>Phone</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>name</td>
            <td>email</td>
            <td>address</td>
            <td>phone</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
}
