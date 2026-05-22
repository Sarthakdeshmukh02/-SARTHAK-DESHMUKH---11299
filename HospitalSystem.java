import java.util.Scanner;

// Class for Patient
class Patient {
    int patientId;
    String name;
    int age;

    Patient(int patientId, String name, int age) {
        this.patientId = patientId;
        this.name = name;
        this.age = age;
    }

    void displayPatient() {
        System.out.println("Patient ID: " + patientId);
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// Class for Appointment
class Appointment {
    int appointmentId;
    String doctorName;
    String date;
    Patient patient;

    Appointment(int appointmentId, String doctorName, String date, Patient patient) {
        this.appointmentId = appointmentId;
        this.doctorName = doctorName;
        this.date = date;
        this.patient = patient;
    }

    void displayAppointment() {
        System.out.println("\n--- Appointment Details ---");
        System.out.println("Appointment ID: " + appointmentId);
        System.out.println("Doctor Name: " + doctorName);
        System.out.println("Date: " + date);
        patient.displayPatient();
    }
}

// Main Class
public class HospitalSystem {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Appointment[] appointments = new Appointment[100]; // 1D Array
        int count = 0; // number of appointments

        int choice;

        do {
            System.out.println("\n===== Hospital Appointment System =====");
            System.out.println("1. Book Appointment");
            System.out.println("2. View Appointments");
            System.out.println("3. Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    if (count >= 100) {
                        System.out.println("Storage Full!");
                        break;
                    }

                    System.out.print("Enter Patient ID: ");
                    int pid = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Enter Patient Name: ");
                    String name = sc.nextLine();

                    System.out.print("Enter Age: ");
                    int age = sc.nextInt();
                    sc.nextLine();

                    Patient p1 = new Patient(pid, name, age);

                    System.out.print("Enter Appointment ID: ");
                    int aid = sc.nextInt();
                    sc.nextLine();

                    System.out.print("Enter Doctor Name: ");
                    String doctor = sc.nextLine();

                    System.out.print("Enter Date: ");
                    String date = sc.nextLine();

                    appointments[count] = new Appointment(aid, doctor, date, p1);
                    count++;

                    System.out.println("Appointment Booked Successfully!");
                    break;

                case 2:
                    if (count == 0) {
                        System.out.println("No Appointments Found!");
                    } else {
                        for (int i = 0; i < count; i++) {
                            appointments[i].displayAppointment();
                        }
                    }
                    break;

                case 3:
                    System.out.println("Exiting System...");
                    break;

                default:
                    System.out.println("Invalid Choice!");
            }

        } while (choice != 3);

        sc.close();
    }
}