package com.example.richard.attendme;

import android.app.ProgressDialog;
import android.content.Context;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.support.v7.widget.Toolbar;
import android.telephony.TelephonyManager;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.MalformedURLException;
import java.net.URL;


public class Register extends AppCompatActivity {

    public String device_id;
    public EditText Stdid;
    public String StdIdStr;
    private ProgressDialog progress;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        Toolbar toolbar = (Toolbar) findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);


        TelephonyManager tm = (TelephonyManager)getSystemService(Context.TELEPHONY_SERVICE);
        device_id = tm.getDeviceId();

        Toast.makeText(this,"IMEI: "+device_id,Toast.LENGTH_LONG).show();

    }


    public  void regis(View view){
        Stdid = (EditText)findViewById(R.id.StudentId);
        StdIdStr = Stdid.getText().toString();
       // device_id = "355884056651846";
        markAttendance(device_id,StdIdStr);

    }

    private void markAttendance(String device_id , String Stdid){
        new PostClass(this).execute();

    }

///Mahita's Code Starts

    private class PostClass extends AsyncTask<String, Void, String> {

        private final Context context;

        public PostClass(Context c){

            this.context = c;
//            this.error = status;
//            this.type = t;
        }
        protected void onPreExecute(){
            progress= new ProgressDialog(this.context);
            progress.setMessage("Loading");
            // progress.show();
        }
        @Override
        protected String doInBackground(String... params) {
            try {

                final TextView outputView = (TextView) findViewById(R.id.showOutput);
                URL url = new URL("http://54.67.55.103:3000/api/registerstudent/");

                HttpURLConnection connection = (HttpURLConnection)url.openConnection();
                String json="";
                String urlParameters1 = StdIdStr;
                String urlParameters2=device_id;

                connection.setRequestMethod("POST");
                connection.setRequestProperty("USER-AGENT", "Mozilla/5.0");
                connection.setRequestProperty("ACCEPT-LANGUAGE", "en-US,en;0.5");
                connection.setDoOutput(true);

                JSONObject jsonObject=new JSONObject();
                jsonObject.accumulate("studentId",urlParameters1);
                jsonObject.accumulate("IMEINum",urlParameters2);
                //jsonObject.put(urlParameters2,true);
                //jsonObject.accumulate(urlParameters1,params[1]);
                // jsonObject.accumulate(urlParameters2,params[2]);
                json=jsonObject.toString();
                DataOutputStream dStream = new DataOutputStream(connection.getOutputStream());
                //dStream.writeBytes(urlParameters1);
                // dStream.writeBytes(urlParameters2);
                dStream.write(json.getBytes());
                dStream.flush();
                dStream.close();
                String responseString = connection.getResponseMessage();
                System.out.println("\nSending 'POST' request to URL : " + url);
                System.out.println("Post parameters : " + urlParameters1);
                System.out.println("Post parameters : " + urlParameters2);
                System.out.println("Response String : " + responseString);
                final StringBuilder output = new StringBuilder("Request URL " + url);
                BufferedReader br = new BufferedReader(new InputStreamReader(connection.getInputStream()));
                String line = "";
                StringBuilder responseOutput = new StringBuilder();

                System.out.println("output===============" + br);
                while((line = br.readLine()) != null ) {
                    responseOutput.append(line);
                }
                br.close();
                output.append(System.getProperty("line.separator") + "Response " + System.getProperty("line.separator") + System.getProperty("line.separator") + responseOutput.toString());
                Register.this.runOnUiThread(new Runnable() {

                    @Override
                    public void run() {
                        outputView.setText(output);
                        progress.dismiss();
                    }
                });
            } catch (MalformedURLException e) {
                e.printStackTrace();
            } catch (IOException e) {
                e.printStackTrace();
            } catch (JSONException e) {
                e.printStackTrace();
            }
            return null;
        }
        protected void onPostExecute() {
            progress.dismiss();
        }
    }


///Mahita's Code Ends

}
