<!-- ButtonComponent.svelte -->
<script>
    import AWS from '../aws/aws-config.js';
    
const handleClick = async () => {
      // Inside handleClick function
    const dynamoDB = new AWS.DynamoDB.DocumentClient();

    const params = {
      TableName: 'pokemon-ratings',
      Item: {
        'id': '123', 'name': 'John Doe'
      },
    };

    try {
      const data = await dynamoDB.put(params).promise();
      console.log('Record created successfully:', data);
    } catch (error) {
      console.error('Error creating record:', error);
    }

    };

  </script>
  
  <button on:click={handleClick}>Create Record</button>


  